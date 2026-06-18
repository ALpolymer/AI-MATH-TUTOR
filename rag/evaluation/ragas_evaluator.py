from dataclasses import dataclass
from typing import Optional, Any
from rag.config import get_config
from openai import AsyncOpenAI
from ragas.embeddings.base import embedding_factory
from ragas.llms import llm_factory
from ragas.metrics.collections import (
    Faithfulness,
    AnswerRelevancy,
    ContextPrecision,
    ContextRecall
    )
import pandas as pd

import asyncio


@dataclass
class RagasSample:
    question: str
    answer: str
    contexts: list[str]
    reference: Optional[str] = None




class RagasEval:
    def __init__(self):
        config = get_config()
        model = config.llm_model
        embedding_model = config.embedding_model
        client = AsyncOpenAI()

        self.llm = llm_factory(model=model, client=client)

        self.embeddings = embedding_factory(
            "openai",
            model=embedding_model,
            client=client,
        )

        self.faithfulness = Faithfulness(llm=self.llm)

        self.answer_relevancy = AnswerRelevancy(
            llm=self.llm,
            embeddings=self.embeddings,
        )

        self.context_precision = ContextPrecision(llm=self.llm)
        self.context_recall = ContextRecall(llm=self.llm)
    
    async def evaluate_one(self, sample: RagasSample) -> dict[str, float | str | None]:
        row: dict[str, float | str | None] = {
            "question": sample.question,
            "answer": sample.answer,
            "reference": sample.reference,
            }

        faithfulness_result = await self.faithfulness.ascore(
            user_input=sample.question,
            response=sample.answer,
            retrieved_contexts=sample.contexts,
        )

        row["faithfulness"] = faithfulness_result.value

        relevancy_result = await self.answer_relevancy.ascore(
            user_input=sample.question,
            response=sample.answer
        )

        row["answer_relevancy"] = relevancy_result.value

        precision_result = await self.context_precision.ascore(
            user_input=sample.question,
            reference=sample.reference,
            retrieved_contexts=sample.contexts
        )

        row["context_precision"] = precision_result.value

        recall_result = await self.context_recall.ascore(
        user_input=sample.question,
        reference=sample.reference,
        retrieved_contexts=sample.contexts,
        )

        row["context_recall"] = recall_result.value

        return row
    

    async def evaluate(self, samples: list[RagasSample]) -> list:
        rows = []
        for sample in samples:
            row = await self.evaluate_one(sample)
            rows.append(row)
        
        return pd.DataFrame(rows)





async def main():
    evaluator = RagasEval()

    sample = RagasSample(
        question="Ποιο είναι το πεδίο ορισμού της f(x) = (x+2)/(x²-3x+2);",
        answer="Η f ορίζεται όταν ο παρονομαστής δεν μηδενίζεται. Το x²-3x+2 έχει ρίζες x=1 και x=2, άρα το πεδίο ορισμού είναι A = ℝ - {1, 2}.",
        contexts=["Η συνάρτηση f ορίζεται όταν x²-3x+2 ≠ 0. Το τριώνυμο x²-3x+2 έχει ρίζες x=1 ή x=2. Επομένως το πεδίο ορισμού της f είναι το σύνολο A = ℝ - {1, 2}."],
        reference="Το πεδίο ορισμού είναι A = ℝ - {1, 2}.",
    )

    result = await evaluator.evaluate([sample, sample])
    print(result)


asyncio.run(main())
