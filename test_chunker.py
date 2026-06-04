from rag.ingestion.loader import MarkdownExerciseLoader
from rag.ingestion.chunker import Chunker
from rag.config import get_config

config = get_config()
loader = MarkdownExerciseLoader(corpus_dir= config.corpus_path)

successful, failed = loader.load()

chunker = Chunker()
processed_docs = chunker.chunk(successful)

print("\n" + "="*40)
print(" METADATA ΤΩΝ CHUNKED DOCUMENTS")
print("="*40)

for doc in processed_docs:
    print("-" * 40)
    for key, value in doc.metadata.items():
        print(f"{key:>20}: {value}")