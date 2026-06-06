from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from rag.retrieval.vector_store import VectorStore
from rag.config import get_config
from rag.generation.prompts import rag_prompt

class ChainBuilder:
    def __init__(self):
        config = get_config()
        model = config.llm_model
        temp = config.temperature

        self.store = VectorStore()
        self.llm = ChatOpenAI(model= model, temperature= temp)
        self.prompt = rag_prompt
        self.generation_chain = self.prompt | self.llm | StrOutputParser()
    
    def _format_docs(self, docs):
        return "\n\n".join(d.page_content for d in docs)
    
    def answer_with_sources(self, question: str) -> dict:
        retrieved_docs = self.store.similarity_search(question)
        context_string = self._format_docs(retrieved_docs)
        answer = self.generation_chain.invoke({ "context" : context_string, "question": question })
        
        return {
            "answer" :  answer,
            "source_docs" :  retrieved_docs
        }