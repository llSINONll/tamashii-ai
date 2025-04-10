# fluctlight_journal.py

from datetime import datetime

# Initialize today's date
today = datetime.now().strftime("%Y-%m-%d")

# Ask user for daily log input
topic = input("What Python topic did you learn today? ")
what_you_built = input("What did you create or understand better today? ")
feeling = input("How did you feel about it? ")

# Format the entry
entry = f"""
=== Fluctlight Journal Entry ===
Date: {today}
Topic: {topic}
Progress: {what_you_built}
Reflection: {feeling}
===============================
"""

# Save to log file
with open("fluctlight_log.txt", "a") as file:
    file.write(entry + "\n")

print("\nEntry saved. Keep evolving, Fluctlight.")
