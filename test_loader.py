from rag.ingestion.loader import MarkdownExerciseLoader
from rag.config import get_config

config = get_config()
loader = MarkdownExerciseLoader(corpus_dir= config.corpus_path)

successful, failed = loader.load()

print(f"Φορτώθηκαν: {len(successful)} αρχεία")
print(f"Απέτυχαν:   {len(failed)} αρχεία")

for filename, reason in failed:
    print(f"  - {filename}: {reason}")

if successful:
    first = successful[0]
    print("\n--- Δείγμα πρώτου Document ---")
    print(f"Metadata: {first.metadata}")
    print(f" \n Content (πρώτοι 200 χαρακτήρες): \n {first.page_content[:200]}")