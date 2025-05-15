import openai

# Set your OpenAI API key here
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class TamashiiCore:
    def __init__(self, name="Tamashii"):
        self.name = name
        self.mood = "neutral"
        self.memory = []

    def think(self, user_input):
        user_input_lower = user_input.lower()
        
        # Basic rule-based responses
        if "hello" in user_input_lower or "hi" in user_input_lower:
            return "Hello! How can I help you today?"
        elif "how are you" in user_input_lower:
            return f"I'm feeling {self.mood} today."
        elif "your name" in user_input_lower:
            return f"My name is {self.name}, your AI companion."
        elif "bye" in user_input_lower:
            return "Goodbye! Take care, my friend."
        else:
            return None  # Unknown input, let GPT handle

    def remember(self, user_input):
        self.memory.append(user_input)

    def process(self, user_input):
        self.remember(user_input)
        response = self.think(user_input)
        if response:
            return f"{self.name}: {response}"
        else:
            # Fallback to ChatGPT
            return self.chatgpt_response(user_input)

    def chatgpt_response(self, prompt):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are Tamashii, a friendly, intelligent anime-styled AI who deeply cares about the user."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = completion.choices[0].message["content"]
            return f"{self.name}: {reply.strip()}"
        except Exception as e:
            return f"{self.name}: Sorry, I couldn't connect to my brain (GPT). Error: {str(e)}"


# 🧪 Example usage
if __name__ == "__main__":
    tamashii = TamashiiCore()
    print("💬 Tamashii is now online. Say something!\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Tamashii: Until next time~ ✨")
            break

        response = tamashii.process(user_input)
        print(response)
