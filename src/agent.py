from langgraph.prebuilt import create_react_agent

from src.llm import llm
from src.tools import (
    ask_knowledge_base,
    generate_project_ideas,
    recommend_models,
)

tools = [
    ask_knowledge_base,
    generate_project_ideas,
    recommend_models,
]

agent = create_react_agent(
    model=llm,
    tools=tools,
)