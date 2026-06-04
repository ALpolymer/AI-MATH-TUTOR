from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from rag.config import get_config


class VectorStore:
    def __init__(self):
        config = get_config()
        embed_model = config.embedding_model
        data_path = config.chroma_db_path
        embedder = OpenAIEmbeddings(model = embed_model)
        self.default_k = config.top_k
        self.store = Chroma(
            persist_directory= str(data_path),
            embedding_function= embedder
        )
        

    def add_documents(self, docs: list[Document]) -> None:
        self.store.add_documents(documents = docs)
    def similarity_search(self, query: str, k : int | None = None) -> list[Document]:
        k_used = k if k is not None else self.default_k
        return self.store.similarity_search(query = query, k= k_used)
        