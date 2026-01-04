from fastapi import APIRouter
from services.embeddingsService import embeddingsService

router = APIRouter()

@router.post("/api/embeddings", summary="Create a new embeddings")
async def create_embeddings_router(chunk: str):
    response = embeddingsService(chunk=chunk)
    return response