from src.llm import llm

response = llm.invoke("Say hello.")

print(response.content)