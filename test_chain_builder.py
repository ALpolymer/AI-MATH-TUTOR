from rag.generation.chain_builder import ChainBuilder

builder = ChainBuilder()

question = "Ποιο είναι το πεδίο ορισμού της f(x) = sqrt(2 - x);"

result = builder.answer_with_sources(question)

print("=" * 50)
print("ΑΠΑΝΤΗΣΗ:")
print(result["answer"])

print("=" * 50)
print("ΠΗΓΕΣ:")
for doc in result["source_docs"]:
        print(f"Σελίδα: {doc.metadata.get('book_page', 'Not found')}, άσκηση: {doc.metadata.get('book_exercise_number', 'Not found')}, υποερώτημα: {doc.metadata.get('source', 'Not Found')}")
