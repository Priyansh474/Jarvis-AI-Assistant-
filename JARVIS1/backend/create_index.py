from pinecone import Pinecone, ServerlessSpec

# Replace with your FULL new key
pc = Pinecone(api_key="pcsk_2XKbNT_your_full_key_here")

index_name = "jarvis-index"   # <- choose this name

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,           # embedding vector size (MiniLM = 384 dims)
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"   # leave default
        )
    )

print("✅ Index Created and Ready:", index_name)
