import subprocess
import os

def execute_agent_task(command):
    """Process system-related commands securely."""
    allowed_commands = ["list", "find", "open", "run", "shutdown"]
    
    # Security check: Only allow specific commands
    if not any(cmd in command.lower() for cmd in allowed_commands):
        return "⚠️ That command is not allowed."

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return f"✅ Command executed:\n{result.stdout}" if result.stdout else "⚠️ No output from command."
    except Exception as e:
        return f"❌ Error: {str(e)}"
import os

def find_file(file_name, search_directory="C:\\Users\\conno\\Documents"):
    """Search for a file in a given directory and return its full path."""
    for root, _, files in os.walk(search_directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return "⚠️ File not found. Check the path or filename."

# Test it:
print(find_file("Lord of the Flies SG1 (1).pdf", "C:\\Users\\conno"))
