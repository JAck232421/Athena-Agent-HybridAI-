import faiss
import numpy as np
import json
from langchain.embeddings import OpenAIEmbeddings

VECTOR_DIM = 768  # Depends on LLM used
index = faiss.IndexFlatL2(VECTOR_DIM)
memory = {}

def store_fact(question, answer):
    """Store facts as vector embeddings."""
    vector = np.random.rand(VECTOR_DIM).astype("float32")  # Placeholder for embedding
    index.add(np.array([vector]))
    memory[len(memory)] = (question, answer)
    with open("memory.json", "w") as f:
        json.dump(memory, f)

def search_memory(question):
    """Search stored knowledge using vector similarity."""
    if not memory:
        return None
    return next((ans for q, ans in memory.values() if q in question), None)
