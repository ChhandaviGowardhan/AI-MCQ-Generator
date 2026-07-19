from pydantic import BaseModel
from typing import List


class MCQ(BaseModel):
    question: str

    option_a: str
    option_b: str
    option_c: str
    option_d: str

    answer: str
    correct_option: str

    explanation: str


class MCQList(BaseModel):
    mcqs: List[MCQ]