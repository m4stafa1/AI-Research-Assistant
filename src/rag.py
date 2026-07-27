from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.llm import llm
from src.prompts import rag_prompt

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | rag_prompt
    | llm
    | StrOutputParser()
)