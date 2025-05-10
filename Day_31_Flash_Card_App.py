#Challenge_1(Flash_Card_App)
'''
🔮 Scenario:
Today, you'll build a simple flash card application to help users
learn new vocabulary. This app will display a word in one language and,
upon user interaction, reveal its translation.

✅ Your Tasks:
Create a GUI window using Tkinter.

Display a word from a predefined list.

Add a button that, when clicked, reveals the translation of the displayed word.

Include a "Next" button to move to the next word in the list.

🧪 Sample Output:
A window displaying the word "こんにちは".

A "Show Translation" button reveals "Hello".

A "Next" button displays the next word, e.g., "ありがとう".
'''
'''
import tkinter as tk
from tkinter import messagebox

# Japanese flashcards list
flashcards = [
    {"Japanese": "こんにちは", "English": "Hello"},
    {"Japanese": "ありがとう", "English": "Thank you"},
    {"Japanese": "さようなら", "English": "Goodbye"},
    {"Japanese": "水", "English": "Water"},
    {"Japanese": "学校", "English": "School"},
    {"Japanese": "猫", "English": "Cat"},
    {"Japanese": "先生", "English": "Teacher"},
]

class FlashCardApp:
    def __init__(self, master):
        self.master = master
        master.title("日本語 Flash Card App")

        self.current_card = 0

        self.word_label = tk.Label(master, text=flashcards[self.current_card]["Japanese"], font=("Helvetica", 36))
        self.word_label.pack(pady=50)

        self.show_button = tk.Button(master, text="英語で表示 (Show Translation)", command=self.show_translation)
        self.show_button.pack()

        self.next_button = tk.Button(master, text="次へ (Next)", command=self.next_card)
        self.next_button.pack(pady=20)

    def show_translation(self):
        translation = flashcards[self.current_card]["English"]
        messagebox.showinfo("Translation", f"{flashcards[self.current_card]['Japanese']} = {translation}")

    def next_card(self):
        self.current_card = (self.current_card + 1) % len(flashcards)
        self.word_label.config(text=flashcards[self.current_card]["Japanese"])

# Create the window
root = tk.Tk()
app = FlashCardApp(root)
root.mainloop()
'''
