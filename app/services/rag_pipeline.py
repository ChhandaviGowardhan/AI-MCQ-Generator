from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


class RAGPipeline:
    """
    Handles:

    Documents
        ↓
    Chunking
        ↓
    Embeddings
        ↓
    Chroma
        ↓
    Retrieval
    """

    def __init__(self):

        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=settings.GEMINI_API_KEY,
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        self.vector_store = Chroma(
            collection_name="mcq_generator",
            embedding_function=self.embedding_model,
            persist_directory="data/chroma_db"
        )

    def build_vector_store(
        self,
        documents: List[Document]
    ) -> int:
        """
        Split documents and store them in Chroma.
        """

        chunks = self.text_splitter.split_documents(
            documents
        )

        # During development, avoid duplicate vectors
        self.vector_store.reset_collection()

        self.vector_store.add_documents(chunks)

        return len(chunks)

    def retrieve_context(
        self,
        top_k: int = 20
    ) -> str:
        """
        Retrieve the most relevant chunks from
        the uploaded document.

        Since this application generates MCQs
        from ONE uploaded document, we use a
        generic query to fetch the most informative
        chunks.
        """

        retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": top_k
            }
        )

        docs = retriever.invoke(
            "Summarize the important concepts from this document."
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        return context