from fastapi import FastAPI
from api.indexRouter import router as api_index_router
from api.embeddingsRouter import router as api_embeddings_router

app = FastAPI()

app.include_router(api_index_router)
app.include_router(api_embeddings_router)