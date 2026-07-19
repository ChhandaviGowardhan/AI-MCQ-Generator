from fastapi import APIRouter, UploadFile, File, Form
import tempfile
import os

from app.services.document_loader import DocumentLoaderService
from app.services.rag_pipeline import RAGPipeline
from app.services.mcq_generator import MCQGenerator

router = APIRouter(
    prefix="/mcq",
    tags=["MCQ Generator"]
)


@router.post("/generate")
async def generate_mcqs(
    file: UploadFile = File(...),
    num_questions: int = Form(5),
    difficulty: str = Form("Medium"),
):
    """
    Upload a PDF and generate MCQs.
    """

    # Save uploaded file temporarily

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:

        temp_file.write(await file.read())

        temp_path = temp_file.name

    try:

        # Load document

        loader = DocumentLoaderService()

        documents = loader.load_document(temp_path)

        # Build Vector Store

        rag = RAGPipeline()

        rag.build_vector_store(documents)

        context = rag.retrieve_context()

        # Generate MCQs

        generator = MCQGenerator()

        result = generator.generate(
            context=context,
            num_questions=num_questions,
            difficulty=difficulty,
        )

        return result.model_dump()

    finally:

        if os.path.exists(temp_path):

            os.remove(temp_path)