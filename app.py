import streamlit as st

from src.agent import agent

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("AI Research Assistant")

    st.markdown("---")

    st.subheader("Knowledge Base")

    st.markdown("""
- 12 AI Research Papers
- Gemini / OpenRouter
- LangGraph Agent
- ChromaDB
- RAG Pipeline
""")

    st.markdown("---")

    st.subheader("Example Questions")

    st.markdown("""
- Explain BERT
- Explain CNN
- Explain RAG
- Explain Vision Transformer
- Explain Attention Mechanism
- Recommend models for Sentiment Analysis
- Generate NLP Project Ideas
""")

    st.markdown("---")

    if st.button("Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

# ==========================================================
# Header
# ==========================================================

st.title("AI Research Assistant")

st.caption(
    "Powered by Gemini • OpenRouter • LangGraph • ChromaDB • RAG"
)

st.success(
    """
Ask anything about:

• Machine Learning

• Deep Learning

• NLP

• Computer Vision

• Transformers

• LLMs

• RAG

• AI Research Papers
"""
)

# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# ==========================================================
# Show Chat History
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"],
            unsafe_allow_html=True,
        )

# ==========================================================
# Chat Input
# ==========================================================

prompt = st.chat_input(
    "Ask anything about AI..."
)



# ==========================================================
# User Message
# ==========================================================

if prompt:

    # -----------------------------
    # Save User Message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -----------------------------
    # Assistant Message
    # -----------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

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

                # -------------------------------------
                # Extract Final Message
                # -------------------------------------

                last_message = response["messages"][-1]

                if hasattr(last_message, "content"):

                    if isinstance(last_message.content, list):

                        answer = ""

                        for item in last_message.content:

                            if (
                                isinstance(item, dict)
                                and item.get("type") == "text"
                            ):

                                answer += item.get("text", "")

                    else:

                        answer = str(last_message.content)

                else:

                    answer = str(last_message)

            except Exception as e:

                error = str(e)

                if (
                    "RESOURCE_EXHAUSTED" in error
                    or "429" in error
                ):

                    answer = """
## Gemini quota exceeded

The Gemini API quota has been exceeded.

The application will automatically use OpenRouter if it is configured correctly.

Otherwise:

- Wait until the quota resets.
- Create a new Gemini API Key.
- Or use another Google account.
"""

                else:

                    answer = f"""
## Unexpected Error

"""

        # -------------------------------------
        # Clean Answer
        # -------------------------------------

        answer = answer.strip()

        # إزالة التكرار إن وجد

        lines = answer.splitlines()

        clean_lines = []

        previous = None

        for line in lines:

            if line.strip() == previous:
                continue

            clean_lines.append(line)

            previous = line.strip()

        answer = "\n".join(clean_lines)

        # -------------------------------------
        # Display
        # -------------------------------------

        placeholder.markdown(
            answer,
            unsafe_allow_html=True,
        )

        # -------------------------------------
        # Save Assistant Message
        # -------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )


# streamlit run app.py

        