import random

EMOTIONS = ["Calm", "Stressed", "Anxious", "Focused", "Fatigued"]

RECOMMENDATIONS = {
    "Calm":     "You are in a great mental state for studying. Keep your routine.",
    "Stressed": "Take a 5-minute deep breathing break. Inhale 4 counts, hold 4, exhale 4.",
    "Anxious":  "Try grounding: name 5 things you see, 4 you touch, 3 you hear.",
    "Focused":  "Excellent focus! Perfect time for your most challenging tasks.",
    "Fatigued": "Your body needs rest. Try a 20-minute power nap or a short walk."
}

def detect_emotion():
    emotion    = random.choice(EMOTIONS)
    confidence = random.randint(70, 90)

    return {
        "emotion":        emotion,
        "confidence":     confidence,
        "recommendation": RECOMMENDATIONS[emotion]
    }
