from .authenticationService import authenticate_pinecone
from pinecone import ServerlessSpec

pc = authenticate_pinecone()

def create_index(name: str):
    pc.create_index(
        name=name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

def list_index():
    response = pc.list_indexes()
    return response.to_dict()

def detail_index(name: str):
    response = pc.describe_index(name=name)
    return response.to_dict()

