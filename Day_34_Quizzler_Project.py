'''
Project Overview:
Create an interactive quiz application that fetches trivia questions from an
online API and presents them to the user in a graphical interface.
The user can answer True/False questions, and the app will keep track
of the score.

🛠️ Technologies & Concepts:
Tkinter: For building the graphical user interface.

Open Trivia Database API: To fetch trivia questions.

Object-Oriented Programming (OOP): To structure the application effectively.

API Integration: Making HTTP requests and handling JSON responses.
'''
import requests
import tkinter as tk
from tkinter import messagebox

# Fetch questions from API
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

# Quiz Logic Class
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = current_question["question"]
        self.correct_answer = current_question["correct_answer"]
        return q_text

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

# GUI Class
class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg="#375362")

        self.score_label = tk.Label(text="Score: 0", fg="white", bg="#375362")
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question will appear here",
            fill="#375362",
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = tk.Button(text="True", width=12, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(text="False", width=12, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            messagebox.showinfo(title="Quiz Complete", message=f"Final Score: {self.quiz.score}/10")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.quiz.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

# Main App
quiz = QuizBrain(question_data)
quiz_ui = QuizInterface(quiz)


