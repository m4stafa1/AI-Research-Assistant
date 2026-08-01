from turtle import st

from src.agent import agent

response = agent.invoke(
    {
        "messages": [
            (
                "human",
                "Explain what is BERT."
            )
        ]
    }
)

st.write(type(response))
st.write(response.keys())

for i, msg in enumerate(response["messages"]):
    st.write(i, type(msg), msg)