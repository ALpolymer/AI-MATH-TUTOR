# 📊 Math Tutor MVP — Progress Tracker

---

### Τρέχουσα κατάσταση

- **Φάση:** 1
- **Τρέχον βήμα:** Βήμα 2 — Basic Indexing (σε εξέλιξη)
- **Status:** `config.py` ολοκληρώθηκε → Επόμενο: `loader.py`

---

### Νέα ολοκληρωμένα βήματα

| #   | Βήμα                           | Notebook ref                     | Ημερομηνία | Σχόλια                                                                       |
| --- | ------------------------------ | -------------------------------- | ---------- | ---------------------------------------------------------------------------- |
| 0   | Project Scaffolding            | —                                | 2026-05-22 | Δομή φακέλων, **init**.py, empty modules                                     |
| 1   | Corpus Preparation             | —                                | 2026-05-22 | 28 λυμένες ασκήσεις, chapter_01_functions, vocabulary.md                     |
| 2a  | `config.py` — Singleton Config | `01_indexing_fundamentals.ipynb` | 2026-05-26 | `@lru_cache`, `@dataclass`, `__post_init__` validation, `repr=False` για key |

---

## 🏗️ Αρχιτεκτονικές Αποφάσεις

- **[2026-05-17]** Corpus scope Φάσης 1 = Κεφάλαιο 1.2 «Συναρτήσεις» του σχολικού βιβλίου.Κρατήσα το scope μικρό για μελλοντική επέκταση.Πεδίο ορισμού, σχετική θέση συναρτήσεων, πράξεις συναρτήσεων, συνθεση και αποσύνθεση συναρτήσεων.
- **[2026-05-17]** Source format = Markdown με LaTeX, γραμμένο χειροκίνητα. Λόγος: καθαρή είσοδος, έλεγχος ποιότητας, καμία εξάρτηση από OCR/PDF conversion.
- **[2026-05-17]** Δομή corpus = ένα markdown αρχείο ανά υποερώτημα (όχι ανά άσκηση). Η κοινή εκφώνηση επαναλαμβάνεται σε κάθε υποερώτημα.
- **[2026-05-17]** Closed vocabulary χωρίς τόνους, lowercase, για όλα τα controlled fields (`topic`, `concepts`, `core_techniques`). Λόγος: αποφυγή διπλών εγγραφών με/χωρίς τόνους.
- **[2026-05-17]** Metadata schema v1

```python
 #(επεκτάσιμη λίστα): definition, theorem_statement, proof, remark, solved_example, solved_exercise.
content_type: solved_exercise
 # Αν το document αναφέρεται σε συγκεκριμένο κεφάλαιο του σχολικού. Αν είναι συνδθαστικό τότε null
chapter: 1.2
 # Αν το document είναι συνδυαστικό τότε αναφέρεται ως syndiastiko
topic: synartiseis
 # Μαθηματικά concepts που χρησιμοποιύνται
concepts:
  - pedio_orismoy
  - synthesi_synartisewn
  - pedio_orismou_synthesis
  - periorismos_rizas
  - trigonometriki_synartisi
  # Μαθηματικές τεχνικές που χρησιμοποιύνται
core_techniques:
  -idiotites_rizwn
  - trigwnometriki_tautotita
  # Βαθμός δυσκολίας (easy, medium, hard)
difficulty: medium
  # Πηγή document(textbook = σχολικό βιβλίο)
source_type: textbook
   # Σελίδα σχολικού στην οποία αντιστοιχεί το document
   # Αν δεν είναι απότο σχολικό, τοτε null
book_page: 28
  # Ομοίως με το book_page
book_exercise_number: "10"
  # Υποερώτημα άσκησης
sub_question: ii
  # Αν το θέμα είναι των πανελληνίων εξετάσεων, τοτε αναφέρεται η χρονιά
exam_year: null
  # Αν το θέμα είναι των πανελληνίων εξετάσεων, τοτε αναφέρεται ποιο θέμα είναι(Α,Β,Γ,Δ)
exam_theme: null
  # Αν το document προήλθε από άλλη πηγη αναφέρεατι εδώ
external_source_name: null
```

- **2026-05-17** Project structure = monorepo, δύο submodules: `rag/` (AI logic, βήματα 1-16) και `backend/` (FastAPI με tiangolo full-stack-fastapi-template structure, βήμα 17). Σήμερα φτιάχνουμε μόνο το `rag/`.
- **2026-05-17** Frontmatter parsing = `python-frontmatter` βιβλιοθήκη. Loader στο `rag/ingestion/loader.py`.

- **2026-05-17** Vocabulary file (`rag/corpus/vocabulary.md`) επεκτείνεται μαζί με το corpus. Κάθε νέα άσκηση που εισάγει νέο concept/technique υποχρεώνει ενημέρωση του vocabulary.

- **2026-05-22** Το top-level package ονομάζεται `rag/` (όχι `math_tutor/`). UI ως `rag/ui/gradio_app.py` (όχι standalone `gradio_app.py`).
- **2026-05-22** Corpus: μόνο solved_exercises προς το παρόν (28 αρχεία .md). Expansion σε επόμενη φάση.
-
- **2026-05-26** `openai_api_key` μπαίνει στο `Config` dataclass (με `repr=False`) για Fail-Fast validation και Single Source of Truth. Δεν διαβάζεται διασκοπρισμένα σε άλλα αρχεία.
- **2026-05-26** `load_dotenv()` καλείται σε module level στο `config.py` — τρέχει μία φορά κατά το import, πριν οριστεί το `Config`.
- **2026-05-26** Paths ορίζονται με `pathlib.Path` relative to `RAG_ROOT = Path(__file__).parent`.

---

### Επόμενα βήματα

1. `rag/ingestion/loader.py` — φόρτωση `.md` αρχείων με YAML frontmatter parsing
2. `rag/ingestion/chunker.py` — chunking strategy για μαθηματικά κείμενα
3. `rag/retrieval/vector_store.py` — ChromaDB persistent setup

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

---

## 📁 Corpus Status

| Item                  | Count | Notes                                |
| --------------------- | ----- | ------------------------------------ |
| Source documents      | _28_  | markdown από σχολικό βιβλίο Ανάλυσης |
| Total chunks          |       |                                      |
| Golden eval questions |       |                                      |
| Coverage chapters     | _1.2_ | _Κεφ. "Όρια & Συνέχεια Συναρτήσεων"_ |

---

## 🎯 Επόμενα Βήματα (next 2-3 actions)

---

## 📝 Decision Log (concise)

---

## 🚧 Φάση 2 — Backlog

- [ ] SymPy integration για math verification
- [ ] Vision input (φωτογράφιση ασκήσεων)
- [ ] Migration σε Qdrant ή pgvector
- [ ] React/TypeScript frontend
- [ ] Καθηγητικό mode (παραλλαγές ασκήσεων)
