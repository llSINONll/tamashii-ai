'''
💡 Concept:
Store past conversations in a list (or dictionary)
and refer back to them for continuity.
Later, you can plug this into an LLM to give your bot
awareness of prior interactions.
'''
import random

emotion_map = {
    "happy": ["glad", "awesome", "joy", "great", "yay"],
    "sad": ["sad", "down", "cry", "unhappy"],
    "angry": ["angry", "mad", "hate", "annoyed"],
    "neutral": []
}

responses = {
    "happy": ["Yatta~! That makes me happy too! 💖", "Hehe~ I'm smiling with you! 🌸"],
    "sad": ["Aww... I'm here if you wanna talk~ 🌧️", "Sending sparkles your way...✨"],
    "angry": ["Let's take a deep breath together 🧘", "It's okay to feel that. I'm with you~"],
    "neutral": ["Ooh, I see~ tell me more! 😃", "Hmm... interesting~ I'm listening! 💬"]
}

conversation_memory = []

def detect_emotion(text):
    text = text.lower()
    for emotion, keywords in emotion_map.items():
        if any(word in text for word in keywords):
            return emotion
    return "neutral"

def tamashii_bot(user_input):
    memory_context = "You said earlier: " + conversation_memory[-1] if conversation_memory else ""
    mood = detect_emotion(user_input)
    reply = random.choice(responses[mood])

    print(f"Tamashii 🤖: {reply}")
    if memory_context:
        print(f"(Memory 🧠: {memory_context})")

    conversation_memory.append(user_input)

# Start chatting
print("Tamashii 🤖: Konbanwa~ I'm here to chat with you 💫 Type 'bye' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Tamashii 🤖: Ja ne~ I'll remember our little talk 🥹")
        break
    tamashii_bot(user_input)
