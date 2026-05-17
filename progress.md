# 📊 Math Tutor MVP — Progress Tracker

> **Πώς χρησιμοποιείται:** Ενημερώνεται στο τέλος κάθε session. Στον Claude λες «Ετοίμασε progress update» και κάνεις paste το αποτέλεσμα στις σχετικές ενότητες. Μετά κάνεις re-upload το αρχείο στο Project knowledge.

---

## 🎯 Τρέχουσα Κατάσταση

**Φάση:** 1 (Maximum AUEB coverage)
**Τρέχον βήμα:** Βήμα 0 — Project scaffolding (σε εξέλιξη)
**Status:** Σε εξέλιξη
**Τελευταία ενημέρωση:** 2026-05-17

---

## ✅ Ολοκληρωμένα Βήματα

| #   | Βήμα                  | Notebook ref | Ημερομηνία   | Σχόλια                            |
| --- | --------------------- | ------------ | ------------ | --------------------------------- |
| 0   | Project scaffolding   | —            | _YYYY-MM-DD_ | _π.χ. Δομή έτοιμη, empty modules_ |
| 1   | Corpus preparation    | —            |              |                                   |
| 2   | Basic indexing        | 3.1          |              |                                   |
| 3   | Vanilla RAG chain     | 3.2          |              |                                   |
| 4   | Evaluation foundation | 2.5, 3.8     |              |                                   |
| 5   | Gradio demo UI        | —            |              |                                   |
| 6   | PCTF + CoT            | 2.3, 2.4     |              |                                   |
| 7   | Structured output     | 2.6          |              |                                   |
| 8   | Query transformations | 3.3          |              |                                   |
| 9   | Routing               | 3.4          |              |                                   |
| 10  | Advanced chunking     | 3.9          |              |                                   |
| 11  | Advanced indexing     | 3.5          |              |                                   |
| 12  | Hybrid + rerank       | 3.6          |              |                                   |
| 13  | Self-correcting RAG   | 3.7          |              |                                   |
| 14  | GraphRAG (optional)   | 3.10         |              |                                   |
| 15  | Safety                | 2.8          |              |                                   |
| 16  | Production basics     | 3.8          |              |                                   |
| 17  | FastAPI wrapper       | 1.6, 1.7     |              |                                   |

---

## 🏗️ Αρχιτεκτονικές Αποφάσεις

> Decisions που πάρθηκαν με τεκμηρίωση. Δεν αλλάζουν εύκολα.

- **[2026-05-17]** Corpus scope Φάσης 1 = ολόκληρο το Κεφάλαιο 1 «Συναρτήσεις» του σχολικού βιβλίου. Λόγος: η σύνθεση συναρτήσεων (αρχικός στόχος) προϋποθέτει πεδίο ορισμού/σύνολο τιμών, άρα standalone scope θα ήταν φτωχό.
- **[2026-05-17]** Source format = Markdown με LaTeX, γραμμένο χειροκίνητα. Λόγος: καθαρή είσοδος, έλεγχος ποιότητας, καμία εξάρτηση από OCR/PDF conversion για το PoC.
- **[2026-05-17]** Δομή corpus = ένα markdown αρχείο ανά υποερώτημα (όχι ανά άσκηση). Η κοινή εκφώνηση επαναλαμβάνεται σε κάθε υπο-αρχείο. Λόγος: clean baseline χωρίς custom splitting code, σωστό citation από το metadata.
- **[2026-05-17]** Closed vocabulary χωρίς τόνους, lowercase, για όλα τα controlled fields (`topic`, `concepts`, `core_techniques`). Λόγος: αποφυγή προβλημάτων encoding και διπλών εγγραφών με/χωρίς τόνους.
- **[2026-05-17]** Metadata schema v1 — τρεις ομάδες fields:
  - **Ομάδα 1 (περιεχόμενο):** content_type, chapter, topic, concepts, core_techniques, difficulty
  - **Ομάδα 2 (πηγή):** source_type
  - **Ομάδα 3 (citation):** book_page, book_exercise_number, sub_question, exam_year, exam_theme, external_source_name
- **[2026-05-17]** Content types (επεκτάσιμη λίστα): definition, theorem_statement, proof, remark, solved_example, solved_exercise, exercise.
- **[2026-05-17]** Project structure = monorepo, δύο submodules: `rag/` (AI logic, βήματα 1-16) και `backend/` (FastAPI με tiangolo full-stack-fastapi-template structure, βήμα 17). Σήμερα φτιάχνουμε μόνο το `rag/`.
- **[2026-05-17]** Frontmatter parsing = `python-frontmatter` βιβλιοθήκη. Loader στο `rag/ingestion/loader.py`.
- **[2026-05-17]** Citation strategy = ξεχωριστά metadata fields (όχι ready-made strings). Το citation string συντίθεται από κώδικα όταν χρειάζεται. Λόγος: ευελιξία στην αλλαγή format χωρίς re-tagging όλου του corpus.
- **[2026-05-17]** Vocabulary file (`rag/corpus/vocabulary.md`) επεκτείνεται μαζί με το corpus. Κάθε νέα άσκηση που εισάγει νέο concept/technique υποχρεώνει ενημέρωση του vocabulary.

---

## ⚙️ Configuration Settings

> Τρέχουσες παράμετροι (αντικατοπτρίζουν το `config.py`)

| Παράμετρος           | Τιμή                                  | Σχόλιο                                         |
| -------------------- | ------------------------------------- | ---------------------------------------------- |
| `chunk_size`         | _π.χ. 800_                            | _Σε χαρακτήρες_                                |
| `chunk_overlap`      | _π.χ. 150_                            |                                                |
| `chunking_strategy`  | _π.χ. RecursiveCharacterTextSplitter_ | _Πειραματίστηκα και με Semantic — δες results_ |
| `embedding_model`    | `text-embedding-3-small`              |                                                |
| `llm_model_primary`  | `gpt-4o-mini`                         |                                                |
| `llm_model_fallback` | `claude-haiku-4-5`                    |                                                |
| `temperature`        | _π.χ. 0.2_                            |                                                |
| `retriever_k`        | _π.χ. 4_                              |                                                |
| `reranker_top_n`     | _π.χ. 3_                              |                                                |

---

## 📊 Evaluation History

> RAGAS metrics από κάθε ολοκληρωμένο βήμα. Δείχνει την εξέλιξη της ποιότητας.

| Βήμα                 | faithfulness | answer_relevancy | context_precision | context_recall | Hit Rate | MRR    | Notes                                |
| -------------------- | ------------ | ---------------- | ----------------- | -------------- | -------- | ------ | ------------------------------------ |
| 3 (vanilla baseline) | _0.72_       | _0.68_           | _0.65_            | _0.70_         | _0.60_   | _0.55_ | _Με 18 ερωτήσεις του golden dataset_ |
| 6 (PCTF added)       |              |                  |                   |                |          |        |                                      |
| 8 (Multi-Query)      |              |                  |                   |                |          |        |                                      |
| 9 (Routing)          |              |                  |                   |                |          |        |                                      |
| 11 (Hybrid+rerank)   |              |                  |                   |                |          |        |                                      |
| 13 (Self-RAG)        |              |                  |                   |                |          |        |                                      |

---

## 🐛 Known Issues & Open Questions

> Πράγματα που δεν δουλεύουν ιδανικά αλλά δεν είναι blockers, ή ανοιχτά ερωτήματα.

- **[YYYY-MM-DD]** _Παράδειγμα: Το LaTeX `\frac{}{}` σπάει σε chunks γιατί το RecursiveCharacterTextSplitter χρησιμοποιεί `\n` ως separator. Σκέφτομαι custom separator list._
- **[YYYY-MM-DD]** _Παράδειγμα: Στις ερωτήσεις περί Bolzano, η ανάκτηση επιστρέφει σχετικά με Rolle επίσης. Πιθανώς χρειάζεται BM25 για ονόματα θεωρημάτων (βήμα 12)._

---

## 📁 Corpus Status

| Item                  | Count | Notes                                  |
| --------------------- | ----- | -------------------------------------- |
| Source documents      | _8_   | _PDF από σχολικό βιβλίο Ανάλυσης ΟΕΔΒ_ |
| Total chunks          | _85_  |                                        |
| Golden eval questions | _18_  | _Από Πανελλήνια 2018-2023_             |
| Coverage chapters     | _1_   | _Κεφ. "Όρια & Συνέχεια Συναρτήσεων"_   |

---

## 🎯 Επόμενα Βήματα (next 2-3 actions)

> Τι σχεδιάζω για την επόμενη session.

1. _Παράδειγμα: Ολοκλήρωση RAGAS evaluation pipeline στο `evaluation/ragas_runner.py`_
2. _Παράδειγμα: Σύνδεση με LangSmith για observability_
3. _Παράδειγμα: Run baseline metrics στο vanilla RAG chain για να έχουμε starting point_

---

## 📝 Decision Log (concise)

> Σύντομες σημειώσεις από κρίσιμες αποφάσεις. Όχι αναλυτικές — απλά «τι» και «γιατί».

- **[YYYY-MM-DD]** _Επέλεξα Propositional chunking για theory documents επειδή η δομή θεωρημάτων ευνοεί atomic facts._
- ...

---

## 🚧 Φάση 2 — Backlog

> Για όταν τελειώσει η Φάση 1. Δεν αγγίζουμε ακόμα.

- [ ] SymPy integration για math verification
- [ ] Vision input (φωτογράφιση ασκήσεων)
- [ ] Migration σε Qdrant ή pgvector
- [ ] React/TypeScript frontend
- [ ] Καθηγητικό mode (παραλλαγές ασκήσεων)
