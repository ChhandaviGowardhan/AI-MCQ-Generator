from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}


class DocumentLoaderService:
    """
    Service responsible for loading and extracting text
    from supported document formats.
    """

    def __init__(self):
        pass

    def load_document(self, file_path: str) -> list[Document]:
        """
        Load a document and return its extracted text.

        Args:
            file_path: Path to uploaded document

        Returns:
            Extracted text
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"{file_path} does not exist."
            )

        extension = path.suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        if extension == ".pdf":
            loader = PyPDFLoader(file_path)

        elif extension == ".docx":
            loader = Docx2txtLoader(file_path)

        else:
            loader = TextLoader(
                file_path,
                encoding="utf-8",
            )

        return loader.load()