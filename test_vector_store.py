from rag.ingestion.loader import MarkdownExerciseLoader
from rag.ingestion.chunker import Chunker
from rag.retrieval.vector_store import VectorStore

from rag.config import get_config

query = "περιορισμός ρίζας"
config = get_config()
loader = MarkdownExerciseLoader(corpus_dir= config.corpus_path)

successful, failed = loader.load()

chunker = Chunker()
processed_docs = chunker.chunk(successful)

store = VectorStore()

store.add_documents(processed_docs)

print(f"Documents στο store: {store.store._collection.count()}")

top_k_docs = store.similarity_search(query)



for doc in top_k_docs:
    print("\n" + "="*40)
    # Προσοχή εδώ: το top_k_docs είναι λίστα. 
    # Τα metadata ανήκουν στο κάθε μεμονωμένο `doc`, όχι στη λίστα!
    print(f"Metadata : {doc.metadata}")
    print(f"Conntent : {doc.page_content[:300]}")