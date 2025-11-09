from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import os

pc = Pinecone(api_key="pcsk_2Ad5ww_NtsZUbuq1VYest4ERi4fiuJEPkL2nnm6YApqvhFSpnSi1FQk2a9PQqXYjZDTfoW")
index = pc.Index("jarvis-index")   # ✅ Correct index name

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(text):
    return embedder.encode(text).tolist()

folder = "data"

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if not os.path.isfile(path):
        continue

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Split the text into smaller chunks
    chunks = content.split("\n\n")
    
    for i, chunk in enumerate(chunks):
        vector = embed(chunk)
        index.upsert([(f"{file}-{i}", vector, {"text": chunk})])

print("✅ Data Ingest Complete!")
