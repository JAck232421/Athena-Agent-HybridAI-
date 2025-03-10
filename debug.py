import subprocess
import traceback
import datetime
import os

# Folder to store backups
BACKUP_FOLDER = "code_backups"
LOG_FILE = "debug_log.txt"

# Ensure backup folder exists
os.makedirs(BACKUP_FOLDER, exist_ok=True)

def backup_code():
    """Save a backup of the current main.py and ai_core.py before making changes."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    files_to_backup = ["main.py", "ai_core.py", "athena_chat.py", "agent_core.py"]

    for file in files_to_backup:
        if os.path.exists(file):
            backup_path = os.path.join(BACKUP_FOLDER, f"{timestamp}_{file}")
            with open("source_file.py", "r", encoding="utf-8") as f:  # Specify UTF-8 encoding
                with open("backup_file.py", "w", encoding="utf-8") as b:
                    b.write(f.read())


def run_athena():
    """Run Athena AI and capture errors."""
    try:
        print("🔄 Running Athena AI...")
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"❌ Athena AI Crashed: {str(e)}\n\n"
        error_message += traceback.format_exc()
        
        # Save error log
        with open(LOG_FILE, "w") as f:
            f.write(error_message)
        
        print("❌ Error detected! Check debug_log.txt for details.")

def suggest_fixes():
    """Read the debug log and try to suggest fixes."""
    if not os.path.exists(LOG_FILE):
        print("✅ No errors detected.")
        return
    
    with open(LOG_FILE, "r") as f:
        error_log = f.read()
    
    print("📜 Debug Log:")
    print(error_log)

    # Basic error handling suggestions
    if "ModuleNotFoundError" in error_log:
        print("💡 Suggestion: You might be missing a package. Try running:")
        print("   pip install -r requirements.txt")

    elif "FileNotFoundError" in error_log:
        print("💡 Suggestion: A required file is missing. Check if all model files are in place.")

    elif "NameError" in error_log:
        print("💡 Suggestion: A variable is not defined. Check for typos in function names or imports.")

    elif "TypeError" in error_log:
        print("💡 Suggestion: A function might be receiving incorrect arguments. Check recent changes.")

    else:
        print("⚠ No direct fix found. Try manually inspecting debug_log.txt.")

def main():
    """Main debugging workflow."""
    backup_code()
    run_athena()
    suggest_fixes()

if __name__ == "__main__":
    main()
