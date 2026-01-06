from fastapi import APIRouter, File, UploadFile
from services.miscellaneousServices import extract_text_from_pdf
from api.miscellaneousRouter import split_in_chunks_embeddings
from services.upsertService import upsertService

router = APIRouter()

@router.post('/api/upsert/pdf', summary='Upsert data into Pinecone')
async def upsert(filepdf: UploadFile = File(...)):
   textfromPDF = extract_text_from_pdf(filepdf)
   chunckslistEmbeddings = await split_in_chunks_embeddings(text=textfromPDF)
   response = upsertService(embeddings=chunckslistEmbeddings)

   return response