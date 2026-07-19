from app.config import settings
from app.gemini_client import client


response = client.models.generate_content(
    model=settings.GEMINI_MODEL,
    contents="Say hello! Tell me if the new project architecture looks clean."
)

print(response.text)