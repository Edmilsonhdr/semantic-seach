from fastapi import APIRouter
from services.queryService import queryService

router = APIRouter()

@router.post('/api/query/simple', summary='Query data from Pinecone')
async def query(search: str):
   response = queryService(search = search)

   matches = response.matches

   json_response = [
    {
        "id": match.id,
        "score": match.score,
        "metadata": match.metadata
    } for match in matches
   ]

   return json_response