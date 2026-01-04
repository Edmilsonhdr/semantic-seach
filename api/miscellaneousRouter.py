from fastapi import APIRouter, File, UploadFile
from services.miscellaneousServices import extract_text_from_pdf

router = APIRouter()

@router.post('/api/miscellaneous/pdf', summary='Extract text from a PDF file')
async def pdf_to_text(filepdf: UploadFile = File(...)):
    text = extract_text_from_pdf(filepdf)
    return text
