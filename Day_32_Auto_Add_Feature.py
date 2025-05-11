'''
🔮 Scenario:
Your flashcard app is looking great! Now let’s give it a cool auto-mode that flips flashcards automatically every few seconds, like a slideshow. Great for passive revision!

✅ Your Task:
Add Auto-Flip Mode:

Add a button that starts automatic flipping every 3 seconds.

It shows the Japanese word ➤ waits 1.5s ➤ shows translation ➤ waits 1.5s ➤ moves to next.

You can use after() method from Tkinter.

Bonus:

Add a “Stop” button to cancel auto-mode.

Add label like “Auto Mode: ON/OFF”.
'''
'''

import tkinter as tk
import random

# Sample Japanese flashcards
flashcards = [
    {"jp": "水", "en": "Water"},
    {"jp": "火", "en": "Fire"},
    {"jp": "風", "en": "Wind"},
    {"jp": "山", "en": "Mountain"},
    {"jp": "空", "en": "Sky"},
]

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Japanese Flashcards")

        self.card_frame = tk.Frame(master)
        self.card_frame.pack(pady=20)

        self.card_text = tk.Label(self.card_frame, text="", font=("Arial", 48))
        self.card_text.pack()

        self.next_button = tk.Button(master, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)

        self.auto_button = tk.Button(master, text="Start Auto Mode", command=self.start_auto_mode)
        self.auto_button.pack()

        self.stop_button = tk.Button(master, text="Stop Auto Mode", command=self.stop_auto_mode)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(master, text="Auto Mode: OFF", fg="gray")
        self.status_label.pack()

        self.current_card = None
        self.showing_english = False
        self.auto_running = False
        self.auto_job = None

        self.next_card()

    def next_card(self):
        self.current_card = random.choice(flashcards)
        self.card_text.config(text=self.current_card["jp"])
        self.showing_english = False

    def flip_card(self):
        if not self.current_card:
            return
        if not self.showing_english:
            self.card_text.config(text=self.current_card["en"])
            self.showing_english = True
        else:
            self.next_card()

    def auto_flip(self):
        if not self.auto_running:
            return
        if not self.showing_english:
            self.flip_card()
            self.auto_job = self.master.after(1500, self.auto_flip)
        else:
            self.next_card()
            self.auto_job = self.master.after(1500, self.auto_flip)

    def start_auto_mode(self):
        if not self.auto_running:
            self.auto_running = True
            self.status_label.config(text="Auto Mode: ON", fg="green")
            self.auto_flip()

    def stop_auto_mode(self):
        if self.auto_running:
            self.auto_running = False
            self.status_label.config(text="Auto Mode: OFF", fg="gray")
            if self.auto_job:
                self.master.after_cancel(self.auto_job)
                self.auto_job = None

# Run the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
'''

