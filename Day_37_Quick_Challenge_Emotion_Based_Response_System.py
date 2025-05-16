'''
✅ What You'll Build:
A mini AI system that:

Takes a user's message

Detects the emotion (happy, sad, angry, etc.)

Responds with a fitting Tamashii-style reply
'''
import random

# Very basic emotion keywords
emotion_map = {
    "happy": ["glad", "awesome", "joy", "great", "yay"],
    "sad": ["sad", "down", "cry", "unhappy"],
    "angry": ["angry", "mad", "hate", "annoyed"],
    "neutral": []
}

responses = {
    "happy": ["Yatta~! I’m so happy with you! 💖", "Hehe! That’s the spirit! 🌸"],
    "sad": ["Aww... Don’t worry, I’m here for you~ 🌧️", "Sending you virtual hugs 🫂"],
    "angry": ["Let’s breathe together... Inhale... Exhale... 💨", "Want to vent a bit more? I’m listening..."],
    "neutral": ["Hmm... interesting~ Tell me more! 😃", "I’m here if you need to talk! 💬"]
}

def detect_emotion(text):
    text = text.lower()
    for emotion, keywords in emotion_map.items():
        if any(word in text for word in keywords):
            return emotion
    return "neutral"

def tamashii_bot(user_input):
    mood = detect_emotion(user_input)
    reply = random.choice(responses[mood])
    print(f"Tamashii 🤖: {reply}")

# Example
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Tamashii 🤖: Mata ne~ ✨")
        break
    tamashii_bot(user_input)
