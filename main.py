from fastapi import FastAPI
from api.indexRouter import router as api_index_router
from api.embeddingsRouter import router as api_embeddings_router
from api.miscellaneousRouter import router as api_miscellaneous_router
from api.upsertRouter import router as api_upsert_router

app = FastAPI()

app.include_router(api_index_router)
app.include_router(api_embeddings_router)
app.include_router(api_miscellaneous_router)
app.include_router(api_upsert_router)