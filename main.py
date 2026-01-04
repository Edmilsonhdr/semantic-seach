from fastapi import FastAPI
from api.indexRouter import router as api_index_router

app = FastAPI()

app.include_router(api_index_router)