from knowledge_base import search_knowledge


question = "Where is the router?"

results = search_knowledge(question)

print("\nRelevant information:\n")

for result in results:

    print("--------------------")
    print(result)