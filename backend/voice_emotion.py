import random

def detect_emotion(text=""):
    emotions = [
        {
            "emotion":        "Calm",
            "recommendation": "You are in a great mental state. Perfect time for focused study."
        },
        {
            "emotion":        "Focused",
            "recommendation": "High focus detected. Use this state for your hardest subjects."
        },
        {
            "emotion":        "Stressed",
            "recommendation": "Stress detected. Take a 10 minute break and breathe deeply."
        },
        {
            "emotion":        "Anxious",
            "recommendation": "Anxiety detected. Try light exercise before studying."
        },
        {
            "emotion":        "Fatigued",
            "recommendation": "Fatigue detected. Rest before your next study session."
        }
    ]

    result               = random.choice(emotions)
    result["confidence"] = random.randint(70, 95)
    return result
