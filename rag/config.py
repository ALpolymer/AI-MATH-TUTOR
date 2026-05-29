
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

CONFIG_FILE_PATH = Path(__file__).resolve()

RAG_ROOT = CONFIG_FILE_PATH.parent

@dataclass
class Config:
    """Application configuration"""
    
    # Paths
    base_path: Path = Path(__file__).parent
    chroma_db_path: Path = RAG_ROOT / "chroma_db"
    corpus_path: Path = RAG_ROOT / "corpus" / "chapter_01_functions"

    # Chunking
    chunk_size: int = 800
    chunk_overlap: int = 150
    separators: List[str] = field(default_factory=lambda: ["\n## ", "\n### ", "\n\n", "\n", " "])

    # --- Metadata (Από το YAML frontmatter) ---
    metadata_keys: List[str] = field(default_factory=lambda: [
        "chapter", "topic", "concepts", "core_techniques", "difficulty"
    ])    

    
    # Retrieval
    top_k: int = 3
    min_relevance_score: float = 0.20
    
    # Embedding
    embedding_model: str = "text-embedding-3-small"
    
    # Generation
    llm_model: str = "gpt-4o-mini"
    max_tokens: int = 800
    temperature: float = 0.1

    openai_api_key: str = field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY"), 
        repr=False
    )
    
    def __post_init__(self):
        
        # Create directories if they don't exist
        self.chroma_db_path.mkdir(exist_ok=True)
        self.corpus_path.mkdir(exist_ok=True)

        if not self.openai_api_key:
            raise ValueError(
                "Το OPENAI_API_KEY δεν βρέθηκε! Βεβαιώσου ότι έχεις ένα αρχείο "
                ".env στον φάκελο του project σου."
            )


@lru_cache()
def get_config() -> Config:
    """Get cached configuration instance"""
    return Config()