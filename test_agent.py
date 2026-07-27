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

print(response["messages"][-1].content)