'''

✅ Features in This Version:
save_memory(thought): Saves thoughts to a file

classify_thought(thought): Determines the type of thought

show_memory(): Reads and displays all past memories

search_memory(keyword): Search through stored memory

'''


import datetime

# Save memory with timestamp and type
def save_memory(thought):
    classification = classify_thought(thought)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_memory.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ({classification}) {thought}\n")
    print("🧠 Tamashii has learned something new!\n")

# Classify the thought
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

# Show all memories
def show_memory():
    print("\n📖 Tamashii Memory Log:\n")
    try:
        with open("tamashii_memory.txt", "r", encoding="utf-8") as file:
            memories = file.readlines()
            for line in memories:
                print(line.strip())
    except FileNotFoundError:
        print("No memory yet. Feed Tamashii's brain!")

# Search for a keyword in memory
def search_memory(keyword):
    print(f"\n🔍 Searching for '{keyword}' in memory:\n")
    try:
        with open("tamashii_memory.txt", "r", encoding="utf-8") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print("Tamashii has no memory yet!")

# Interface Loop
def main():
    print("🧠 Welcome to Tamashii Brain v2\n")
    while True:
        print("\nOptions:")
        print("1. Teach Tamashii a new thought")
        print("2. Show memory")
        print("3. Search memory")
        print("4. Exit\n")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            thought = input("What do you want to teach Tamashii? ➤ ")
            save_memory(thought)

        elif choice == '2':
            show_memory()

        elif choice == '3':
            keyword = input("What keyword do you want to search? ➤ ")
            search_memory(keyword)

        elif choice == '4':
            print("🌙 Tamashii will sleep now. Mata ne~")
            break

        else:
            print("Please choose a valid option!")

if __name__ == "__main__":
    main()
