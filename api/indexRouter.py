from fastapi import APIRouter
from services.indexService import create_index, list_index

router = APIRouter()

@router.post("/api/index/create")
async def create_index_router(name_index: str):
    create_index(name_index)
    return {"message": f"Index {name_index} created successfully"}

@router.get("/api/index/list")
async def list_index_router():
    return list_index()