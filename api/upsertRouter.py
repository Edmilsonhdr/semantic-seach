from fastapi import APIRouter, File, UploadFile, Form
from services.miscellaneousServices import extract_text_from_pdf
from api.miscellaneousRouter import split_in_chunks_embeddings, split_in_chunks
from services.upsertService import upsertService, upsertService_metadata
import json

router = APIRouter()

@router.post('/api/upsert/pdf', summary='Upsert data into Pinecone')
async def upsert(filepdf: UploadFile = File(...)):
   textfromPDF = extract_text_from_pdf(filepdf)
   chunckslistEmbeddings = await split_in_chunks_embeddings(text=textfromPDF)
   response = upsertService(embeddings=chunckslistEmbeddings)

   return response

@router.post('/api/upsert/pdf_metadata', summary='Upsert data into Pinecone')
async def upsert_metadata(filepdf: UploadFile = File(...), metadata: str = Form(...)):
   metadataJson = json.loads(metadata)
   textfromPDF = extract_text_from_pdf(filepdf)
   chunkslistText = await split_in_chunks(text=textfromPDF)
   response = upsertService_metadata(metadata=metadataJson, chunkslistText=chunkslistText)

   return {"message": f"Data upserted successfully", "count": response}