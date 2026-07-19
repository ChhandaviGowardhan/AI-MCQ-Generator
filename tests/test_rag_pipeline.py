from app.services.document_loader import DocumentLoaderService
from app.services.rag_pipeline import RAGPipeline

loader = DocumentLoaderService()

documents = loader.load_document("data/sample.pdf")

rag = RAGPipeline()

chunks = rag.build_vector_store(documents)

print(f"Chunks stored: {chunks}")

context = rag.retrieve_context()

print("=" * 60)

print(context[:2000])