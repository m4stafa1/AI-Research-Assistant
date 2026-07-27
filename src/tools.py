from langchain_core.tools import tool

from src.rag import rag_chain
from src.llm import llm


@tool
def ask_knowledge_base(question: str) -> str:
    """
    Answer questions using the local AI knowledge base.
    """
    return rag_chain.invoke(question)


@tool
def generate_project_ideas(domain: str) -> str:
    """
    Generate AI project ideas.
    """

    prompt = f"""
    Generate 5 AI project ideas in {domain}.

    For each project provide:
    - Project title
    - Difficulty
    - Dataset
    - Recommended models
    - Skills learned
    """

    return llm.invoke(prompt).content


@tool
def recommend_models(task: str) -> str:
    """
    Recommend ML/DL models for a task.
    """

    prompt = f"""
    Recommend the best machine learning or deep learning models for:

    {task}

    Explain why each model is suitable.
    """

    return llm.invoke(prompt).content