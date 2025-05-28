'''
🔮 Add a Minimal Graphical Interface for Tamashii using tkinter
You'll be able to:

✅ Talk to Tamashii with text

✅ See her responses in a beautiful window

✅ Display last 3 emotional replies for "visual memory"

'''

import tkinter as tk
from tkinter import scrolledtext
import openai
import datetime

openai.api_key = "sk-xxxxxxxxxxxx"

# --- Emotion classifier ---
def classify_emotion(text):
    emotions = ["happy", "sad", "curious", "angry", "motivated", "anxious"]
    prompt = f"Classify the emotion of this sentence: '{text}' — only return one of {emotions}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an emotion classifier."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().lower()

# --- Memory handler ---
def save_memory(user_msg, ai_reply, user_emotion, ai_emotion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tamashii_gui_memory.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] 🧍‍♂️ {user_emotion} You: {user_msg}\n")
        file.write(f"             🤖 {ai_emotion} Tamashii: {ai_reply}\n\n")

def get_recent_memories(lines=3):
    try:
        with open("tamashii_gui_memory.txt", "r", encoding="utf-8") as file:
            all_lines = file.readlines()
            return ''.join(all_lines[-lines*2:])  # 2 lines per memory
    except FileNotFoundError:
        return ""

# --- GPT Response ---
def get_response(msg, context=""):
    prompt = f"Memory:\n{context}\n\nYou: {msg}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Tamashii, an emotional and kind AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- GUI Setup ---
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return

    user_emotion = classify_emotion(user_msg)
    memory = get_recent_memories()
    ai_reply = get_response(user_msg, memory)
    ai_emotion = classify_emotion(ai_reply)

    chat_log.insert(tk.END, f"You ({user_emotion}): {user_msg}\n")
    chat_log.insert(tk.END, f"Tamashii ({ai_emotion}): {ai_reply}\n\n")
    chat_log.yview(tk.END)

    save_memory(user_msg, ai_reply, user_emotion, ai_emotion)
    entry.delete(0, tk.END)

# --- TK App ---
root = tk.Tk()
root.title("🧠 Tamashii AI - Emotional Companion")
root.geometry("500x500")

chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=5)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

root.mainloop()
