import openai
import datetime

# Replace with your OpenAI API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

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

def save_memory(thought):
    classification = classify_thought(thought)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_memory.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ({classification}) {thought}\n")

def show_memory():
    try:
        with open("tamashii_memory.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def auto_memory_decision(message, reply):
    # Ask GPT if this reply should be saved
    prompt = (
        f"User said: {message}\n"
        f"AI replied: {reply}\n\n"
        "Based on this conversation, should the AI save the reply as an important memory for the user?\n"
        "Answer with only 'yes' or 'no'."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a smart memory filter."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().lower() == "yes"

def chat_with_tamashii_gpt(prompt, memory_context=""):
    system_prompt = (
        "You are Tamashii, a wise personal AI assistant. Use the memory to make responses more helpful.\n\n"
        f"Memory Context:\n{memory_context}\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- MAIN LOOP ---
def main():
    print("🤖 Tamashii Brain v3.5 – Smart Auto-Memory 🧠")

    while True:
        print("\nOptions:\n1. Talk to Tamashii\n2. Show memory\n3. Exit")
        choice = input("➤ Choose (1/2/3): ")

        if choice == "1":
            message = input("\n🗨️ You: ")
            memory = "".join(show_memory()[-10:])  # last 10 lines
            reply = chat_with_tamashii_gpt(message, memory)
            print("🧠 Tamashii:", reply)

            if auto_memory_decision(message, reply):
                save_memory(reply)
                print("💾 Thought auto-saved!")

        elif choice == "2":
            print("\n📚 Tamashii Memory Log:")
            for line in show_memory():
                print(line.strip())

        elif choice == "3":
            print("🌙 Tamashii is resting... Sayonara~")
            break

        else:
            print("⚠️ Invalid input. Try 1, 2, or 3.")

if __name__ == "__main__":
    main()
