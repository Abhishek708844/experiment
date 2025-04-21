from fastapi import FastAPI
from .schemas import MessageResponse

app = FastAPI(title="DevOps Experiment API")

@app.get("/", response_model=MessageResponse)
async def root():
    return {"message": "Welcome to DevOps Experiment API"}

@app.get("/health", response_model=MessageResponse)
async def health_check():
    return {"message": "API is healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}