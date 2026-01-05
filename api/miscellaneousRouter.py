from fastapi import APIRouter, File, UploadFile
from services.miscellaneousServices import extract_text_from_pdf, slip_text_into_chunks

router = APIRouter()

@router.post('/api/miscellaneous/pdf', summary='Extract text from a PDF file')
async def pdf_to_text(filepdf: UploadFile = File(...)):
    text = extract_text_from_pdf(filepdf)
    return text

@router.post('/api/miscellaneous/slip_text_into_chunks', summary='Slip text into chunks')
async def slip_in_chunks(text: str):
    response = slip_text_into_chunks(text)
    return response