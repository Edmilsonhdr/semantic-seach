from pinecone.grpc import PineconeGRPC as Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

def authenticate_pinecone():
    return Pinecone(api_key=os.getenv("PINECONE_API_KEY"))





