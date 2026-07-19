from fastapi import FastAPI

from app.routers.mcq import router as mcq_router

app = FastAPI(
    title="AI Powered MCQ Generator",
    version="1.0.0",
)

app.include_router(mcq_router)


@app.get("/")
def home():

    return {
        "message": "AI Powered MCQ Generator API"
    }