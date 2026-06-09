import frontmatter
from typing import List, Optional
from pathlib import Path
from pydantic import ValidationError, BaseModel, Field
from langchain_core.documents import Document


class ExerciseFrontmatter(BaseModel):
    content_type: str = Field(description="Ο τύπος του περιεχομένου, π.χ. solved_exercise")
    chapter: str
    topic: str
    concepts: List[str] = Field(default_factory = list)
    core_techniques: List[str] = Field(default_factory=list)
    source_type: str
    difficulty: str
    book_page: Optional[int] = None
    book_exercise_number: Optional[str] = None
    sub_question: Optional[str] = None
    exam_year: Optional[int] = None
    exam_theme: Optional[str] = None
    external_source_name: Optional[str] = None

class MarkdownExerciseLoader:
    def __init__(self, corpus_dir: str | Path):
        self.corpus_dir = Path(corpus_dir)
    
    def load(self) -> tuple[List[Document], List[tuple[str, str]]]:
        successful = []
        failed = []
        for file_path in self.corpus_dir.glob("*.md"):
            try:
                parsed_file = frontmatter.load(file_path)

                validated_metadata = ExerciseFrontmatter(**parsed_file.metadata)

                final_metadata = validated_metadata.model_dump()
                final_metadata["source"] = file_path.name

                doc = Document(
                    page_content = parsed_file.content.strip(),
                    metadata=final_metadata
                )

                successful.append(doc)

            except ValidationError as e: 
                failed.append((file_path.name, f"Failed Schema (Missing field or type errors {str(e)})"))
            
            except Exception as e:
                failed.append((file_path.name, f"Σφάλμα Ανάγνωσης: {str(e)}"))
                
        return successful, failed