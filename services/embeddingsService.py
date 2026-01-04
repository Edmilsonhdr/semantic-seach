from services.authenticationService import authenticate_gemini

client = authenticate_gemini()

def embeddingsService(chunk: str):
    result = client.models.embed_content(
        model="text-embedding-004",
        contents=[chunk]
    )
    return result.embeddings[0].values
