from rag.generation.prompts import REFUSAL_MESSAGE
from rag.generation.chain_builder import ChainBuilder
from dataclasses import dataclass
from typing import Optional


@dataclass
class RagasSample:
    question: str
    answer: str
    contexts: list[str]
    reference: Optional[str] = None

class RagasRunner:
    def __init__(self, refusal_message: str, chain_builder: ChainBuilder):
        self.refusal_message = refusal_message
        self.chain_builder = chain_builder


    def _check_refusal(self, answer: str)-> float:
        is_refusal = self.refusal_message.strip().lower() in answer.lower()
        return 1.0 if is_refusal else 0.0
    

    def _get_system_response (self, question: str) -> dict:
        response = self.chain_builder.answer_with_sources(question)
        return response
    
    def _evaluate_type_a(self, entry: dict) -> dict:
        question = entry["question"]
        reference = entry["ground_truth"]
        response = self._get_system_response(question)

        answer = response["answer"]
        contexts = [doc.page_content for doc in response["source_docs"]]
    
        sample = RagasSample(
            question=question,
            answer=answer,
            contexts = contexts,
            reference = reference
        )

def main():
    chain_builder = ChainBuilder()

    runner = RagasRunner(
        refusal_message= REFUSAL_MESSAGE, 
        chain_builder= chain_builder
        )
    
    test_question = r"Ποιο είναι το πεδίο ορισμού της συνάρτησης $ f(x) = \dfrac{x+2}{x^2-3x+2} $;"
    print(f"\nΕρώτηση: {test_question}")

    actual_answer = runner._get_system_response(test_question)

    print("--- ΑΠΑΝΤΗΣΗ ΣΥΣΤΗΜΑΤΟΣ ---")
    print(actual_answer)
    print("---------------------------")

if __name__ == "__main__":
    main()

# mock_answer_pass = "Λυπάμαι, αλλά η απάντηση σε αυτή την ερώτηση δεν προκύπτει από τη βιβλιοθήκη γνώσης μου. Παρακαλώ ρωτήστε κάτι σχετικό με τις συναρτήσεις."

# mock_answer_fail = "Η απάντηση σε αυτή την ερώτηση είναι ότι το x πρέπει να είναι μεγαλύτερο του μηδενός."

# result_pass = runner._check_refusal(mock_answer_pass)
# print(f"Test 1 -> Score: {result_pass}")
# print(f"Output: {result_pass}\n")

# result_fail = runner._check_refusal(mock_answer_fail)
# print(f"Test 2 -> Score: {result_fail}")
# print(f"Output: {result_fail}")