# AI-Powered MCQ Generator 

An end-to-end Retrieval-Augmented Generation (RAG) application that automatically generates high-quality Multiple Choice Questions (MCQs) from uploaded PDF documents using **Google Gemini**, **LangChain**, **ChromaDB**, **FastAPI**, and **Streamlit**.

The application extracts text from uploaded documents, creates semantic embeddings, stores them in a vector database, retrieves the most relevant context using Retrieval-Augmented Generation (RAG), and leverages Google's Gemini Large Language Model to generate structured MCQs with answers and explanations.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Google Gemini Embeddings
- 🗂️ ChromaDB Vector Database
- 🔍 Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini LLM
- ✅ Structured MCQ generation
- 📥 Download MCQs as JSON
- 📊 Download MCQs as CSV
- 🌐 REST API using FastAPI
- 💻 Interactive Streamlit frontend

---

# Architecture

```

                PDF Upload
                     │
                     ▼
          Document Loader (LangChain)
                     │
                     ▼
      Recursive Text Splitter
                     │
                     ▼
       Gemini Embedding Model
                     │
                     ▼
             ChromaDB Vector Store
                     │
                     ▼
          Similarity Search (RAG)
                     │
                     ▼
            Gemini Flash LLM
                     │
                     ▼
       Structured MCQ Generation
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
     FastAPI API            Streamlit UI

```

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | Google Gemini Flash |
| Embeddings | Gemini Embedding Model |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Document Loading | LangChain Document Loaders |
| Text Splitting | RecursiveCharacterTextSplitter |
| Data Validation | Pydantic |
| API Testing | Swagger UI |

---

# Project Structure

```

MCQ-Project/
│
├── app/
│   ├── models/
│   │   └── mcq_models.py
│   │
│   ├── prompts/
│   │   └── mcq_prompt.py
│   │
│   ├── routers/
│   │   └── mcq.py
│   │
│   ├── services/
│   │   ├── document_loader.py
│   │   ├── rag_pipeline.py
│   │   └── mcq_generator.py
│   │
│   ├── config.py
│   ├── gemini_client.py
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── sample.pdf
│
├── tests/
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md

```

---

# How It Works

## Step 1 — Upload PDF

The user uploads a PDF document through the Streamlit interface.

↓

## Step 2 — Document Loading

The application extracts text using LangChain document loaders.

↓

## Step 3 — Text Chunking

The extracted text is split into overlapping chunks using Recursive Character Text Splitter.

↓

## Step 4 — Embedding Generation

Each chunk is converted into dense vector embeddings using the Google Gemini Embedding model.

↓

## Step 5 — Vector Storage

The embeddings are stored inside ChromaDB for semantic retrieval.

↓

## Step 6 — Retrieval-Augmented Generation (RAG)

Relevant chunks are retrieved using similarity search.

↓

## Step 7 — MCQ Generation

The retrieved context is passed to Gemini Flash LLM, which generates structured multiple-choice questions.

↓

## Step 8 — Output

Generated MCQs include:

- Question
- Four options
- Correct answer
- Correct option text
- Explanation

Users can download the results as JSON or CSV.

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-MCQ-Generator.git

cd AI-MCQ-Generator
```

---

Create a virtual environment

```bash
python -m venv mcq
```

Activate it

Windows

```bash
mcq\Scripts\activate
```

Linux / macOS

```bash
source mcq/bin/activate
```

---

Install dependencies

```bash
pip install -r requirements.txt
```

---

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

# Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend will be available at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

```bash
streamlit run frontend/app.py
```

The application will launch in your browser.

---

# API Endpoint

## Generate MCQs

```
POST /mcq/generate
```

### Form Data

| Field | Type |
|---------|------|
| file | PDF |
| num_questions | Integer |
| difficulty | Easy / Medium / Hard |

---

# Example Response

```json
{
  "mcqs": [
    {
      "question": "Which algorithm is commonly used for customer segmentation?",
      "option_a": "Linear Regression",
      "option_b": "Random Forest",
      "option_c": "K-Means",
      "option_d": "Naive Bayes",
      "answer": "C",
      "correct_option": "K-Means",
      "explanation": "K-Means is an unsupervised clustering algorithm commonly used for customer segmentation."
    }
  ]
}
```

---

# Sample Application Flow

1. Upload a PDF document.
2. Select the difficulty level.
3. Choose the number of questions.
4. Click **Generate MCQs**.
5. Review generated questions and explanations.
6. Download results as JSON or CSV.

---

# Future Enhancements

- Support for DOCX and TXT uploads
- Question categorization by topic
- Bloom's Taxonomy question generation
- Difficulty estimation using LLM
- User authentication
- MCQ export to PDF
- Answer shuffling
- Question history
- Multi-document retrieval
- Persistent vector database

---

# Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Google Gemini API
- LangChain
- Vector Databases
- Semantic Search
- Prompt Engineering
- FastAPI
- Streamlit
- REST API Development
- Pydantic
- Document Processing
- AI Application Development

---

# Screenshots

You can add screenshots here after running the application.

```
Home Screen

frontend/screenshots/home.png
```

```
Generated MCQs

frontend/screenshots/result.png
```
---

# Author

**Chhandavi Gowardhan**

Python | Data Analytics | AI | Machine Learning | NLP | FastAPI | Streamlit | LangChain

GitHub: [https://github.com/YOUR_USERNAME](https://github.com/ChhandaviGowardhan)

LinkedIn: [https://linkedin.com/in/YOUR_PROFILE](https://www.linkedin.com/in/chhandavi-gowardhan-56b458291/)
