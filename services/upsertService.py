from services.authenticationService import authenticate_pinecone
from services.embeddingsService import embeddingsService
import uuid

pc = authenticate_pinecone()

def upsertService(embeddings: list):
    index = pc.Index(host="https://itvalleydados-912p7qa.svc.aped-4627-b74a.pinecone.io")
    try:
        vectors = []
        for chuck_unit in embeddings:
            vectors.append({"id": f"{uuid.uuid4()}", "values": chuck_unit})

            response = index.upsert(
                vectors = vectors,
                namespace = "master-ia-pos"
            )
            return {"message": "Data upserted successfully"}
    except Exception as e:
        return {"message": "Error upserting data", "error": str(e)}

def upsertService_metadata(metadata: dict, chunkslistText: list):
    index = pc.Index(host="https://itvalleydados-912p7qa.svc.aped-4627-b74a.pinecone.io")
    vectors = []
    try:
        for chunkstext in chunkslistText:
            embeddingschunk = embeddingsService(chunkstext)
            metadatacomplete = {**metadata, "chunk": chunkstext}

            vectors.append({"id": f"{uuid.uuid4()}", "values": embeddingschunk, "metadata": metadatacomplete})

            response = index.upsert(
                vectors = vectors,
                namespace = "master-ia-pos"
            )
            return response.upserted_count
    except Exception as e:
        return {"message": "Error upserting data", "error": str(e)}