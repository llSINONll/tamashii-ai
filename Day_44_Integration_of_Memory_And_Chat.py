'''
Tamashii Brain v2.5 – Memory + Chat Integration (Offline)
We’ll add a very simple offline conversation mode using your stored memory and a few basic responses.
Later we’ll plug in ChatGPT API or LLMs, but today: offline + logic-based replies.

✅ What We’ll Do:
User can say anything

Tamashii checks memory and replies smartly

Replies vary based on:

Keyword in user message

If memory contains related entries

Or general fallback response
'''

import datetime

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

def search_memory(keyword):
    memory = show_memory()
    results = [line for line in memory if keyword.lower() in line.lower()]
    return results

# Simple logic-based chat engine
def chat_with_tamashii(message):
    keywords = ["ai", "japan", "language", "study", "happy", "sad"]
    memory = show_memory()

    for key in keywords:
        if key in message.lower():
            matches = search_memory(key)
            if matches:
                return f"Tamashii remembers something about '{key}':\n" + matches[-1]
            else:
                return f"Tell me more about {key} — I'd love to remember it."

    return "That's interesting! Would you like to save this thought into my memory?"

# Interface
def main():
    print("🤖 Tamashii Brain v2.5: Offline AI with memory\n")

    while True:
        print("\nOptions:")
        print("1. Talk to Tamashii")
        print("2. Show memory")
        print("3. Exit")
        choice = input("➤ Choose (1/2/3): ")

        if choice == "1":
            message = input("\n🗨️ You: ")
            response = chat_with_tamashii(message)
            print("🧠 Tamashii:", response)

            save = input("💾 Save this thought to memory? (yes/no): ").lower()
            if save.startswith("y"):
                save_memory(message)
                print("📚 Thought saved.")

        elif choice == "2":
            print("\n🧠 Tamashii Memory Log:")
            for line in show_memory():
                print(line.strip())

        elif choice == "3":
            print("🌙 Tamashii will rest now. Mata ne~")
            break

        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
