# 📊 Math Tutor MVP — Progress Tracker

---

### Τρέχουσα κατάσταση

- **Φάση:** 1
- **Τρέχον βήμα:** Βήμα 2 — Basic Indexing (chunker ✓, vector_store επόμενο)
- **Status:** Σε εξέλιξη

---

### Deadline & πλάνο

- **Deadline καθηγητή:** 20 Ιουνίου 2026 — ελάχιστο παραδοτέο.
- **Διαθέσιμος χρόνος:** ~5-6 ώρες/μέρα.
- **Πηγή απαιτήσεων:** AUEB Final Project spec (FastAPI backend + ουσιαστικό GenAI + λειτουργικό UI + GitHub/docs/README).

### Scope ελάχιστου παραδοτέου (MVP για 20/6)

1. `vector_store.py` — ChromaDB persistent (boilerplate, γρήγορα)
2. Vanilla RAG chain — notebook 3.2 (Σωκρατικά, η ουσία)
3. PCTF system prompt — notebook 2.4 (Σωκρατικά, ελαφρύ)
4. Gradio UI — thin layer (γίνεται δεκτό από spec, όχι React)
5. FastAPI backend — /chat endpoint + schemas + error handling + Swagger (boilerplate, γρήγορα)
6. Documentation (PDF) + README.md + .gitignore + requirements.txt + παραδείγματα
7. RAGAS: ΜΙΑ baseline μέτρηση για το documentation (όχι gate ανά βήμα)

### Εκτός ελάχιστου scope (μελλοντικές επεκτάσεις στο documentation)

- Βήματα 7-16: query transformations, routing, hybrid search, reranking, self-correcting RAG (LangGraph), GraphRAG, production basics.
- **Stretch goal** (μόνο αν στέκει το ελάχιστο νωρίς): ένα από Multi-Query / self-query routing με τα metadata.

### Νέα ολοκληρωμένα βήματα

| #   | Βήμα                                                                                           | Notebook ref                              | Ημερομηνία | Σχόλια                                                                                                                                                                                                   |
| --- | ---------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Project Scaffolding                                                                            | —                                         | 2026-05-22 | Δομή φακέλων, **init**.py, empty modules                                                                                                                                                                 |
| 1   | Corpus Preparation                                                                             | —                                         | 2026-05-22 | 28 λυμένες ασκήσεις, chapter_01_functions, vocabulary.md                                                                                                                                                 |
| 2a  | `config.py` — Singleton Config                                                                 | `01_indexing_fundamentals.ipynb`          | 2026-05-26 | `@lru_cache`, `@dataclass`, `__post_init__` validation, `repr=False` για key                                                                                                                             |
| 2b  | `rag/ingestion/loader.py` — `MarkdownExerciseLoader` + `ExerciseFrontmatter` (Pydantic schema) | Module 3 / 01_indexing_fundamentals.ipynb | 2026-05-29 | OOP class-based. python-frontmatter parsing + Pydantic validation. Επιστρέφει `tuple[List[Document], List[tuple[str, str]]]` — Επιλογή Β (collect-all-errors). Δοκιμάστηκε σε 28 αρχεία, 28/28 επιτυχία. |
| 2c  | `rag/ingestion/chunker.py` — `Chunker.chunk()`                                                 | `01_indexing_fundamentals.ipynb`          | 2026-06-04 | 1 αρχείο = 1 chunk, no splitting. Προσθέτει `chunk_index=0` + `total_chunks=1` στα metadata. Έτοιμο για μελλοντικό splitting θεωρίας. Τεσταρίστηκε σε 28/28 με ξεχωριστό script.                         |

## 🏗️ Αρχιτεκτονικές Αποφάσεις

- **[2026-05-17]** Corpus scope Φάσης 1 = Κεφάλαιο 1.2 «Συναρτήσεις» του σχολικού βιβλίου.Κρατήσα το scope μικρό για μελλοντική επέκταση.Πεδίο ορισμού, σχετική θέση συναρτήσεων, πράξεις συναρτήσεων, συνθεση και αποσύνθεση συναρτήσεων.
- **[2026-05-17]** Source format = Markdown με LaTeX, γραμμένο χειροκίνητα. Λόγος: καθαρή είσοδος, έλεγχος ποιότητας, καμία εξάρτηση από OCR/PDF conversion.
- **[2026-05-17]** Δομή corpus = ένα markdown αρχείο ανά υποερώτημα (όχι ανά άσκηση). Η κοινή εκφώνηση επαναλαμβάνεται σε κάθε υποερώτημα.
- **[2026-05-17]** Closed vocabulary χωρίς τόνους, lowercase, για όλα τα controlled fields (`topic`, `concepts`, `core_techniques`). Λόγος: αποφυγή διπλών εγγραφών με/χωρίς τόνους.
- **[2026-05-17]** Metadata schema v1

- **[2026-05-29]** OOP class-based προσέγγιση για όλα τα modules του core. Συναρτήσεις μόνο για helpers.
- **[2026-05-29]** Loader strategy: collect-all-errors. Δύο "καλάθια" (`successful`, `failed`) αντί για fail-fast. Λόγος: πιο βολικό για manual curation των 28 αρχείων.
- **[2026-05-29]** Δύο ξεχωριστές κλάσεις στο `loader.py`: `ExerciseFrontmatter` (Pydantic schema) και `MarkdownExerciseLoader` (το "I/O") — αυστηρό Single Responsibility.
- **[2026-05-29]** `concepts` και `core_techniques` αποθηκεύονται ως native `list[str]` στα metadata (Chroma >= 1.5.0 υποστηρίζει arrays με `$contains` / `$not_contains` operators). Καμία flattening μετατροπή.

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

- **2026-06-04** Δεν γίνεται splitting στη Φάση 1 — τα solved_exercise documents είναι ήδη αυτοτελή (1 υποερώτημα + εκφώνηση + λύση = 1 αρχείο). Το chunking έγινε de facto στο corpus design, όχι στον κώδικα.
- **2026-06-04** `chunk_index` / `total_chunks` αντί για `is_chunked: bool`. Λόγος: ο ακέραιος δείκτης κρατά θέση μέσα σε ακολουθία (χρήσιμο όταν μπει θεωρία που σπάει σε N chunks)· το `is_chunked` προκύπτει παράγωγα (`total_chunks > 1`).
- **2026-06-04** Ιδιοκτησία εννοιών: τα `chunk_index`/`total_chunks` τα βάζει ο **chunker**, όχι ο loader (Single Responsibility — η έννοια "chunk" γεννιέται στον chunker).
- **2026-06-04** Ο `chunk()` τροποποιεί τα metadata **in-place** και επιστρέφει την ίδια λίστα (συνειδητή επιλογή για Φάση 1· τα Document objects είναι κοινά references με την έξοδο του loader).
- **2026-06-04** RAGAS υποβαθμίστηκε από "gate ανά βήμα" σε "μία baseline + μία τελική μέτρηση για documentation". Λόγος: 28 docs + vanilla RAG δεν δίνουν αρκετό σήμα ανά μικρο-βήμα· πιο νοηματική αφήγηση για το docs.
- **2026-06-04** UI = Gradio για το ελάχιστο (επιβεβαιωμένα δεκτό από spec). React μετατίθεται σε Φάση 2.

---

### Επόμενα βήματα

1. **Βήμα 2d** — `rag/retrieval/vector_store.py` (ChromaDB persistent, `data/chroma_db/`).

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

- **[2026-05-29]** Open question για Βήμα 9 (Routing): το LangChain `ChromaTranslator` του self-query retriever ίσως **δεν** υποστηρίζει `$contains` operator πάνω σε list metadata fields. Αν παίξει πρόβλημα τότε, ίσως χρειαστεί custom translator ή αλλαγή αναπαράστασης. Δεν επηρεάζει το τωρινό βήμα.

---

## 📁 Corpus Status

| Item                  | Count | Notes                                |
| --------------------- | ----- | ------------------------------------ |
| Source documents      | _28_  | markdown από σχολικό βιβλίο Ανάλυσης |
| Total chunks          |       |                                      |
| Golden eval questions |       |                                      |
| Coverage chapters     | _1.2_ | _Κεφ. "Όρια & Συνέχεια Συναρτήσεων"_ |

---
