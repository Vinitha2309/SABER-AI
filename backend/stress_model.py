def predict_stress(study_hours, sleep_hours, mood):
    score = 0

    if study_hours > 10:
        score += 40
    elif study_hours > 7:
        score += 20
    elif study_hours > 5:
        score += 10

    if sleep_hours < 5:
        score += 40
    elif sleep_hours < 6:
        score += 25
    elif sleep_hours < 7:
        score += 10

    mood_scores = {
        "happy":   0,
        "neutral": 10,
        "sad":     25,
        "anxious": 35,
        "angry":   30
    }
    score += mood_scores.get(mood.lower(), 10)

    stress_risk  = min(score, 100)
    burnout_risk = min(int(stress_risk * 0.9), 100)

    if stress_risk >= 70:
        level = "high"
        message = "High burnout risk detected. Immediate action recommended."
        recommendations = [
            "Reduce study hours to under 6 per day",
            "Get at least 8 hours of sleep tonight",
            "Take a 30 minute break every 2 hours",
            "Talk to a counselor or trusted friend"
        ]
    elif stress_risk >= 40:
        level = "medium"
        message = "Moderate stress levels. Monitor your wellbeing."
        recommendations = [
            "Aim for 7 to 8 hours of sleep",
            "Include short breaks in your study sessions",
            "Try light exercise or a short walk",
            "Eat regular healthy meals"
        ]
    else:
        level = "low"
        message = "Low stress levels. Keep up the good work!"
        recommendations = [
            "Maintain your current sleep schedule",
            "Continue balanced study habits",
            "Stay hydrated throughout the day",
            "Keep your mood positive with activities you enjoy"
        ]

    return {
        "stressRisk":      stress_risk,
        "burnoutRisk":     burnout_risk,
        "level":           level,
        "message":         message,
        "recommendations": recommendations
    }
