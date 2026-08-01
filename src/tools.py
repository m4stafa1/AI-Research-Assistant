from langchain_core.tools import tool

from src.rag import rag_chain
from src.llm import llm


# ==========================================================
# Knowledge Base Tool
# ==========================================================

@tool
def ask_knowledge_base(question: str) -> str:
    """
    Search the local AI knowledge base and answer the user's question.
    Always use this tool for AI concepts, papers, ML, DL, NLP, CV,
    Transformers, LLMs, RAG, and related topics.
    """

    try:

        answer = rag_chain.invoke(question)

        if not answer or len(answer.strip()) == 0:
            return (
                "I couldn't find enough information in the knowledge base."
            )

        return answer

    except Exception as e:

        return f"Knowledge Base Error:\n{str(e)}"


# ==========================================================
# Project Ideas Tool
# ==========================================================

@tool
def generate_project_ideas(domain: str) -> str:
    """
    Generate practical AI project ideas for a specific domain.
    """

    prompt = f"""
You are an experienced AI mentor.

Generate 5 high-quality AI project ideas for:

{domain}

For each project provide:

# Project Title

## Difficulty
Beginner / Intermediate / Advanced

## Description

## Dataset

## Recommended Models

## Skills Learned

## Expected Outcome

Format everything in Markdown.
"""

    try:

        return llm.invoke(prompt).content

    except Exception as e:

        return f"Project Generator Error:\n{str(e)}"


# ==========================================================
# Model Recommendation Tool
# ==========================================================

@tool
def recommend_models(task: str) -> str:
    """
    Recommend the best ML/DL models for a given task and explain why.
    """

    prompt = f"""
You are an AI Engineer.

Recommend the best Machine Learning or Deep Learning models for:

{task}

For each model provide:

# Model Name

## Why use it

## Advantages

## Limitations

## Best Use Cases

## Difficulty

## Libraries

Return the answer in Markdown.
"""

    try:

        return llm.invoke(prompt).content

    except Exception as e:

        return f"Recommendation Error:\n{str(e)}"