from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings
from app.models.mcq_models import MCQList
from app.prompts.mcq_prompt import MCQ_PROMPT


class MCQGenerator:

    def __init__(self):

        llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3,
        )

        # Structured output
        self.llm = llm.with_structured_output(MCQList)

        self.prompt = ChatPromptTemplate.from_template(
            MCQ_PROMPT
        )

    def generate(
        self,
        context: str,
        num_questions: int = 5,
        difficulty: str = "Medium",
    ):

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "num_questions": num_questions,
                "difficulty": difficulty,
            }
        )

        return response