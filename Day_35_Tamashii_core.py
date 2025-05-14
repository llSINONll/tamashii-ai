'''
🔹 Build the Core Brain Class of Tamashii
Like TamashiiCore that will:

Accept user input (eventually from speech)

Process using OpenAI (or mock for now)

Return a Japanese-style reply (optionally bilingual)
'''
class TamashiiCore:
    def __init__(self):
        self.name = "Tamashii"
        self.mood = "calm"
        self.version = "0.1-dev"

    def process_input(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input:
            return "こんにちは、ご主人様！(Hello, Master!)"
        
        elif "how are you" in user_input or "元気" in user_input:
            return "私は元気ですよ！あなたは？(I'm doing well! How about you?)"
        
        elif "who are you" in user_input:
            return f"私は魂AIのコアです。名前は{self.name}、バージョン{self.version}です！(I'm the core of Tamashii AI. Name: {self.name}, Version: {self.version})"
        
        elif "love" in user_input:
            return "愛は最も強力な魔法ですね 💖 (Love is the strongest magic, isn't it?)"
        
        elif "bye" in user_input or "さようなら" in user_input:
            return "さようなら、ご主人様！またお会いしましょう。(Goodbye, Master! See you again!)"
        
        else:
            return "すみません、それはまだ学習していません... (Sorry, I haven't learned that yet...)"

# 🧪 Example Interaction
if __name__ == "__main__":
    tamashii = TamashiiCore()
    print("💫 Tamashii.AI 起動完了。ご主人様、いかがなさいましたか？")

    while True:
        user = input("You: ")
        response = tamashii.process_input(user)
        print(f"Tamashii: {response}")
        
        if "bye" in user.lower() or "さようなら" in user:
            break

