import streamlit as st
from src.agent import agent

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title(" AI Research Assistant")

    st.markdown("---")

    st.markdown("###  Knowledge Base")

    st.info("""
 12 Research Papers

 Gemini Flash

 ChromaDB

 RAG + LangGraph
""")

    st.markdown("---")

    st.markdown("###  Sample Questions")

    st.markdown("""
- Explain BERT
- Explain CNN
- Explain RAG
- Explain YOLO
- What is Attention?
- Recommend models for Sentiment Analysis
- Generate NLP Project Ideas
""")

    st.markdown("---")

    if st.button(" Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ==========================
# Main Page
# ==========================

st.title(" AI Research Assistant")

st.caption("Powered by Gemini + LangGraph + RAG + ChromaDB")

st.success(
    "Welcome! Ask me anything about Artificial Intelligence, Machine Learning, Deep Learning, NLP, Computer Vision, or RAG."
)

# ==========================
# Chat History
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================
# User Input
# ==========================

prompt = st.chat_input("Ask your question...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = agent.invoke(
                    {
                        "messages": [
                            (
                                "human",
                                prompt,
                            )
                        ]
                    }
                )

                last_message = response["messages"][-1]

                if isinstance(last_message.content, list):

                    answer = ""

                    for item in last_message.content:

                        if (
                            isinstance(item, dict)
                            and item.get("type") == "text"
                        ):
                            answer += item.get("text", "")

                else:

                    answer = last_message.content

            except Exception as e:

                error_text = str(e)

                if (
                    "RESOURCE_EXHAUSTED" in error_text
                    or "429" in error_text
                ):

                    answer = """
##  Gemini API Quota Exceeded

The free Gemini API quota has been reached.

Please try one of the following:

- Wait a few minutes and try again.
- Create a new Gemini API Key.
- Use another Google account.

Your application is working correctly. Only the API quota has been exceeded.
"""

                else:

                    answer = f"""
##  Unexpected Error """

