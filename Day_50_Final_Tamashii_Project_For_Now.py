import tkinter as tk
from tkinter import scrolledtext
import openai
import datetime
import pyttsx3  # Text-to-Speech

# Set your OpenAI key here
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 165)

# --- Emotion classifier ---
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

# --- Memory handling ---
def save_memory(user_msg, ai_reply, user_emotion, ai_emotion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_memory_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] 🧍‍♂️ ({user_emotion}) You: {user_msg}\n")
        file.write(f"             🤖 ({ai_emotion}) Tamashii: {ai_reply}\n\n")

def get_recent_memories(n=3):
    try:
        with open("tamashii_memory_log.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            return ''.join(lines[-n*2:])
    except FileNotFoundError:
        return ""

# --- GPT Response handler ---
def get_response(message, context=""):
    prompt = f"Memory:\n{context}\n\nYou: {message}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Tamashii, a kind emotional AI that helps humans and remembers emotional context."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- GUI App Logic ---
def send_message():
    user_msg = entry.get()
    if not user_msg.strip():
        return

    user_emotion = classify_emotion(user_msg)
    memory = get_recent_memories()
    ai_reply = get_response(user_msg, memory)
    ai_emotion = classify_emotion(ai_reply)

    chat_log.insert(tk.END, f"You ({user_emotion}): {user_msg}\n")
    chat_log.insert(tk.END, f"Tamashii ({ai_emotion}): {ai_reply}\n\n")
    chat_log.yview(tk.END)

    save_memory(user_msg, ai_reply, user_emotion, ai_emotion)

    # Speak the response
    engine.say(ai_reply)
    engine.runAndWait()

    entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("🧠 Tamashii AI - Final Memory Form")
root.geometry("500x520")

chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=5)

send_btn = tk.Button(root, text="Talk to Tamashii 💬", command=send_message)
send_btn.pack(pady=5)

root.mainloop()
