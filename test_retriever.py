from src.rag import retriever

docs = retriever.invoke("What is Retrieval-Augmented Generation?")

print(f"Number of documents: {len(docs)}")

for i, doc in enumerate(docs):
    print("=" * 50)
    print(f"Document {i+1}")
    print("=" * 80)
    print(doc.page_content)