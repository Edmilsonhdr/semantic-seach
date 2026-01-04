from fastapi import APIRouter
from services.indexService import create_index, list_index, detail_index

router = APIRouter()

@router.post("/api/index/create", summary="Create a new index")
async def create_index_router(name_index: str):
    create_index(name_index)
    return {"message": f"Index {name_index} created successfully"}

@router.get("/api/index/list", summary="List all indexes")
async def list_index_router():
    return list_index()

@router.get("/api/index/detail", summary="Detail a index")
async def detail_index_router(name: str):
    return detail_index(name)

