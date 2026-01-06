from fastapi import APIRouter, File, UploadFile
from services.miscellaneousServices import extract_text_from_pdf
from services.miscellaneousServices import slip_text_into_chunks
from services.embeddingsService import embeddingsService

router = APIRouter()

@router.post('/api/miscellaneous/pdf', summary='Extract text from a PDF file')
async def pdf_to_text(filepdf: UploadFile = File(...)):
    text = extract_text_from_pdf(filepdf)
    return text

@router.post('/api/miscellaneous/split_in_chunks', summary='Slip text into chunks')
async def split_in_chunks(text: str):
    response = slip_text_into_chunks(text=text)
    return response

@router.post('/api/miscellaneous/split_in_chunks_embeddings', summary='Slip text into chunks for embeddings')
async def split_in_chunks_embeddings(text: str):
    chunk_list = slip_text_into_chunks(text=text)

    embeddings = []
    for chunk in chunk_list:
        embeddings.append(embeddingsService(chunk=chunk))
    return embeddings