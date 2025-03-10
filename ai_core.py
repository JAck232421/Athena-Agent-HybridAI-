import re
from athena_chat import ask_athena
from system_agent import execute_agent_task

# Default mode is chatbot
MODE = "chatbot"

# Define keywords that suggest Agent mode
AGENT_KEYWORDS = ["open", "execute", "run", "list", "install", "shutdown", "restart", "search", "find", "kill", "terminate"]
CHATBOT_KEYWORDS = ["who", "what", "where", "when", "why", "how", "tell me", "define", "joke", "fact", "history", "explain"]

def infer_mode(query):
    """Infer whether to use Agent mode or Chatbot mode based on keywords."""
    global MODE
    if query.lower().startswith("agent:"):
        MODE = "agent"
        return "agent"
    elif query.lower().startswith("athena:"):
        MODE = "chatbot"
        return "chatbot"
    
    if any(word in query.lower() for word in AGENT_KEYWORDS):
        MODE = "agent"
        return "agent"
    elif any(word in query.lower() for word in CHATBOT_KEYWORDS):
        MODE = "chatbot"
        return "chatbot"

    return MODE  # If ambiguous, keep the last used mode

def process_input(user_input):
    """Route query to the correct mode."""
    mode = infer_mode(user_input)
    if mode == "chatbot":
        return ask_athena(user_input.replace("Athena:", "").strip())
    elif mode == "agent":
        return execute_agent_task(user_input.replace("Agent:", "").strip())
    else:
        return "Invalid mode."
