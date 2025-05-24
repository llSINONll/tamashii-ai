import openai
import datetime

# Paste your OpenAI API key here
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def save_memory(thought):
    classification = classify_thought(thought)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_memory.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ({classification}) {thought}\n")

def classify_thought(thought):
    thought = thought.lower()
    if any(word in thought for word in ["learn", "studied", "understood"]):
        return "Learning"
    elif any(word in thought for word in ["happy", "sad", "angry", "feeling"]):
        return "Emotion"
    elif any(word in thought for word in ["japan", "language", "ai", "python"]):
        return "Fact"
    else:
        return "General"

def show_memory():
    try:
        with open("tamashii_memory.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def chat_with_tamashii_gpt(prompt, memory_context=""):
    system_prompt = (
        "You are Tamashii, a personal AI assistant who remembers the user's thoughts, dreams, and goals. "
        "Always answer warmly and wisely. Use memory context if relevant.\n\n"
        f"Memory Context:\n{memory_context}\n"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Interface
def main():
    print("🤖 Tamashii Brain v3.0: With GPT 💡")

    while True:
        print("\nOptions:")
        print("1. Talk to Tamashii")
        print("2. Show memory")
        print("3. Exit")
        choice = input("➤ Choose (1/2/3): ")

        if choice == "1":
            message = input("\n🗨️ You: ")
            memory = "".join(show_memory()[-10:])  # last 10 memories
            reply = chat_with_tamashii_gpt(message, memory)
            print("🧠 Tamashii:", reply)

            save = input("💾 Save this to memory? (yes/no): ").lower()
            if save.startswith("y"):
                save_memory(message)
                print("📚 Thought saved.")

        elif choice == "2":
            print("\n🧠 Tamashii Memory Log:")
            for line in show_memory():
                print(line.strip())

        elif choice == "3":
            print("🌙 Tamashii is powering down... See you tomorrow~")
            break

        else:
            print("⚠️ Invalid input. Try again.")

if __name__ == "__main__":
    main()
