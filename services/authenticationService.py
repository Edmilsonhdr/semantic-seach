from pinecone.grpc import PineconeGRPC as Pinecone
import os
from dotenv import load_dotenv
from openai import OpenAI
import google.genai as genai

load_dotenv()

def authenticate_pinecone():
    return Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def authenticate_openai():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def authenticate_gemini():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY ou GOOGLE_API_KEY não encontrada no arquivo .env")
    client = genai.Client(api_key=api_key)
    return client

