'''
Add Voice Input and Output
🗣️ Talk to Tamashii — and she’ll listen and reply with a real voice.

✅ Features for Today:
🎙️ Speech-to-Text using speech_recognition

🔊 Text-to-Speech using pyttsx3 (offline & fast)
'''

import speech_recognition as sr
import pyttsx3
import openai
import datetime

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# Set your API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def speak(text):
    print("Tamashii 🧠:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You 🗣️:", text)
            return text
        except sr.UnknownValueError:
            print("⚠️ Couldn't understand.")
            return ""
        except sr.RequestError:
            print("❌ Speech API unavailable.")
            return ""

def classify_thought(thought):
    thought = thought.lower()
    if any(w in thought for w in ["learn", "studied", "understood"]):
        return "Learning"
    elif any(w in thought for w in ["happy", "sad", "feeling"]):
        return "Emotion"
    elif any(w in thought for w in ["japan", "language", "ai", "python"]):
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
    prompt = (
        f"User said: {message}\n"
        f"AI replied: {reply}\n\n"
        "Should the reply be saved as an important memory? Answer 'yes' or 'no'."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a memory filter."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().lower() == "yes"

def chat_with_tamashii_gpt(prompt, memory_context=""):
    system_prompt = (
        "You are Tamashii, a voice-enabled personal AI assistant. Use memory to help user better.\n\n"
        f"Memory:\n{memory_context}\n"
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
    print("🎙️ Tamashii v4.0 – Voice Mode Activated 🌸")
    while True:
        print("\nOptions:\n1. Talk with Voice\n2. Show Memory\n3. Exit")
        choice = input("➤ Choose (1/2/3): ")

        if choice == "1":
            message = listen()
            if message:
                memory = "".join(show_memory()[-10:])
                reply = chat_with_tamashii_gpt(message, memory)
                speak(reply)

                if auto_memory_decision(message, reply):
                    save_memory(reply)
                    print("💾 Memory auto-saved.")

        elif choice == "2":
            print("\n📚 Tamashii Memory:")
            for line in show_memory():
                print(line.strip())

        elif choice == "3":
            speak("Sayonara Sahil! Tamashii is powering down.")
            break

        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
