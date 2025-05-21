'''
🔥 Challenge: Guess the Number AI Mode!
But wait — you’ve already played guessing games...
What if YOU write the AI that guesses the number you think of?

🤖 Game: AI Tries to Guess Your Number
Let’s flip the roles:

You secretly pick a number between 1 and 100

The AI guesses

You just say: "too high", "too low", or "correct"

💡 Concepts:
Binary Search Logic

Loops + Conditions

Simulated Intelligence

'''

def ai_guess_number():
    print("🧠 Think of a number between 1 and 100 (don't tell me!)")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"🤖 AI guesses: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"🎉 AI guessed it in {attempts} tries!")
            break
        else:
            print("❌ Invalid input. Please type H, L, or C.")

ai_guess_number()
