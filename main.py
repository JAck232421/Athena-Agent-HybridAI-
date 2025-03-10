from ai_core import process_input

while True:
    user_input = input("\n📝 Enter command (Athena: [question] / Agent: [command]): ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = process_input(user_input)
    print(f"\n🔹 Response:\n{response}")
