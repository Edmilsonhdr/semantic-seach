from PyPDF2 import PdfReader
from fastapi import FastAPI
from io import BytesIO

def extract_text_from_pdf(filepdf: bytes):
    #read the file - BytesIO
    pdf_byte = filepdf.file.read()

    #create a PDF reader
    pdf_stream = BytesIO(pdf_byte)

    readerPDF = PdfReader(pdf_stream)
    text = ""
    for page in readerPDF.pages:
        text += page.extract_text()
    return text

def slip_text_into_chunks(text: str, chunk_size: 1000, overlap: 200) -> list:
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks