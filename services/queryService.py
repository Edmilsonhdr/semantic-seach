from services.authenticationService import authenticate_pinecone
from services.embeddingsService import embeddingsService

def queryService(search: str):
    pc = authenticate_pinecone()
    try:
       vectors = embeddingsService(search)

       index = pc.Index(host="https://itvalleydados-912p7qa.svc.aped-4627-b74a.pinecone.io")
       response = index.query(
           namespace="master-ia-pos",
           vector=vectors,
           top_k=10,
           include_metadata=True
       )
       
       return response
    except Exception as e:
        return {"message": "Error querying data", "error": str(e)}