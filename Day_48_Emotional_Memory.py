'''
🧩 "Emotional Memory" System
Tamashii can now remember:

How you felt when you said something

How she felt when she responded

'''


import random
import openai
import datetime
import pyttsx3
import speech_recognition as sr

openai.api_key = "sk-xxxxxxxxxxxx"

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Tamashii 🧠: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You 🗣️: {text}")
            return text
        except:
            print("😵 Couldn't catch that.")
            return ""

def classify_emotion(text):
    emotions = ["happy", "sad", "curious", "angry", "motivated", "anxious"]
    prompt = f"Classify the emotion of this sentence: '{text}' — only return one of {emotions}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an emotion classifier."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip().lower()

def save_memory_emotion(message, reply, user_emotion, ai_emotion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_emotions.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] 🧍‍♂️ You ({user_emotion}): {message}\n")
        file.write(f"             🤖 Tamashii ({ai_emotion}): {reply}\n\n")

def show_memories():
    try:
        with open("tamashii_emotions.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def get_response(message, memory):
    context = "".join(memory[-10:])
    system_prompt = f"You are Tamashii, a kind emotional AI assistant.\n\nPrevious emotions:\n{context}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("💖 Tamashii v5 – Emotional AI is LIVE")
    while True:
        print("\nOptions:\n1. Talk\n2. Show Memory\n3. Exit")
        choice = input("➤ ")

        if choice == "1":
            message = listen()
            if message:
                user_emotion = classify_emotion(message)
                mem = show_memories()
                reply = get_response(message, mem)
                ai_emotion = classify_emotion(reply)

                speak(reply)
                save_memory_emotion(message, reply, user_emotion, ai_emotion)

        elif choice == "2":
            print("📚 Emotional Memory:")
            for line in show_memories():
                print(line.strip())

        elif choice == "3":
            speak("Goodbye, Sahil! Tamashii loves your energy!")
            break

if __name__ == "__main__":
    main()

