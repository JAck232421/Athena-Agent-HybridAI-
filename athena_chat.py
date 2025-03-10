import json
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from llm_model import generate_response

# Load Memory
MEMORY_FILE = "athena_memory.json"
def load_memory():
    """Load Athena's stored memory."""
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"chat_history": ""}

def save_memory(memory):
    """Save memory to JSON file."""
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

athena_memory = load_memory()


from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize Embeddings Model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

try:
    # Load existing FAISS index
    vector_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
except Exception as e:
    print("FAISS index not found. Creating a new one...")
    # Create an empty FAISS index safely
    vector_db = FAISS.from_texts(["Placeholder"], embeddings)
    vector_db.save_local("faiss_index")



# Define Prompt
prompt_template = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
Athena is a highly intelligent AI assistant designed to provide accurate and reliable information.
- She NEVER makes up information.
- If she does not know something, she will clearly say, "I don't know."
- She follows the user's commands strictly and asks for clarification if needed.
- She can recall facts from memory but ONLY if they were explicitly told to her.

Conversation History:
{chat_history}
User: {user_input}
Athena:
"""
)

def ask_athena(question):
    """Ask Athena a factual question with RAG support."""
    global athena_memory

    # Use RAG (Retrieval-Augmented Generation)
    qa_chain = RetrievalQA(llm=generate_response, retriever=retriever, prompt=prompt_template)

    response = qa_chain.run({"chat_history": athena_memory["chat_history"], "user_input": question})
    
    if "I don't know" in response:
        return "I'm not sure. Can you provide more details?"

    athena_memory["chat_history"] += f"\nUser: {question}\nAthena: {response}"
    save_memory(athena_memory)
    
    return response
