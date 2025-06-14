from pipeline import process_pipeline

if __name__ == "__main__":
    print("AI Pipeline – Titan Text (Amazon Bedrock)")
    while True:
        user_input = input("\nEnter input (or type 'exit'): ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        result = process_pipeline(user_input)
        print("\nFinal Output:\n", result)
