from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pinecone Setup
pc = Pinecone(api_key="pcsk_2Ad5ww_NtsZUbuq1VYest4ERi4fiuJEPkL2nnm6YApqvhFSpnSi1FQk2a9PQqXYjZDTfoW")
index = pc.Index("jarvis-index")

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

LLAMA_API_URL = "http://127.0.0.1:5001/v1/chat/completions"

class Query(BaseModel):
    query: str

def embed(text):
    return embedder.encode(text).tolist()

@app.post("/query")
async def query_api(data: Query):
    query_vec = embed(data.query)

    search = index.query(vector=query_vec, top_k=3, include_metadata=True)

    context = "\n\n".join([match["metadata"]["text"] for match in search.matches if "text" in match.metadata])

    payload = {
        "model": "koboldcpp",
        "messages": [
            {"role": "system", "content": f"You are JARVIS. Use the following context when answering:\n\n{context}"},
            {"role": "user", "content": data.query}
        ]
    }

    response = requests.post(LLAMA_API_URL, json=payload).json()
    answer = response["choices"][0]["message"]["content"]
    return {"response": answer}
