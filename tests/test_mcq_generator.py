from app.services.document_loader import DocumentLoaderService
from app.services.rag_pipeline import RAGPipeline
from app.services.mcq_generator import MCQGenerator

loader = DocumentLoaderService()
documents = loader.load_document("data/sample.pdf")

rag = RAGPipeline()

rag.build_vector_store(documents)

context = rag.retrieve_context()

generator = MCQGenerator()

result = generator.generate(
    context=context,
    num_questions=5,
    difficulty="Medium",
)

print(result.model_dump_json(indent=4))