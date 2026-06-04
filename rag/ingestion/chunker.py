from langchain_core.documents import Document


class Chunker:
    def chunk(self, docs: list[Document]) -> list[Document]:
        for doc in docs:
            doc.metadata["chunk_index"] = 0
            doc.metadata["total_chunks"] = 1
        return docs    