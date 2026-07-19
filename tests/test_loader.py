from app.services.document_loader import DocumentLoaderService

loader = DocumentLoaderService()

documents = loader.load_document("data/sample.pdf")

print(documents[0].page_content[:1000])