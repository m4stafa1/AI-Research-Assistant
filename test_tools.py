from src.tools import (
    ask_knowledge_base,
    generate_project_ideas,
    recommend_models,
)

print("=" * 80)
print(ask_knowledge_base.invoke("What is BERT?"))

print("=" * 80)
print(generate_project_ideas.invoke({"domain": "Computer Vision"}))

print("=" * 80)
print(recommend_models.invoke({"task": "Image Classification"}))