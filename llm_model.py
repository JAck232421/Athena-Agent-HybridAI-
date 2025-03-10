from langchain_community.llms import LlamaCpp

# Path to your GGUF model (Update this to your actual model file)
MODEL_PATH = r"C:\Athena-Agent Hybrid AI\mistral-7b-instruct-v0.2.Q8_0.gguf"

# Load Local Llama Model
llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_gpu_layers=35,
    n_threads=8,
    n_batch=512,
    n_ctx=4096,
    verbose=True
)

def generate_response(prompt):
    """Run local LLM on the given prompt"""
    return llm.invoke(prompt)
