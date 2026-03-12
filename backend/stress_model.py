def predict_stress(study_hours, sleep_hours, mood,
                   assignments_due=0, exercise_minutes=0):

    score = 0

    # Study load factor
    if study_hours > 8:
        score += 35
    elif study_hours > 6:
        score += 20
    elif study_hours > 4:
        score += 10

    # Sleep deficit factor
    if sleep_hours < 5:
        score += 40
    elif sleep_hours < 6:
        score += 25
    elif sleep_hours < 7:
        score += 10

    # Mood factor
    if mood == "sad":
        score += 25
    elif mood == "neutral":
        score += 10

    # Assignment pressure
    if assignments_due > 3:
        score += 20
    elif assignments_due > 1:
        score += 10

    # Exercise relief
    if exercise_minutes > 30:
        score -= 10
    elif exercise_minutes > 15:
        score -= 5

    stress_risk  = max(0, min(score, 100))
    burnout_risk = max(0, min(stress_risk + (10 if study_hours > 6 else -5), 100))

    # Determine level
    if stress_risk < 30:
        level = "low"
        message = "You are managing stress well!"
    elif stress_risk < 55:
        level = "medium"
        message = "Moderate stress detected — take small breaks."
    elif stress_risk < 75:
        level = "high"
        message = "High stress level — reduce workload immediately."
    else:
        level = "critical"
        message = "Critical burnout risk — take a full rest day!"

    # Build recommendations
    recommendations = []
    if sleep_hours < 7:
        recommendations.append("Aim for 7–9 hours of sleep per night")
    if study_hours > 6:
        recommendations.append("Use the Pomodoro technique (25 min study, 5 min break)")
    if mood == "sad":
        recommendations.append("Practice mindfulness or meditation for 10 minutes daily")
    if exercise_minutes < 20:
        recommendations.append("Add at least 20–30 minutes of physical activity to your day")
    if assignments_due > 2:
        recommendations.append("Prioritize tasks using the Eisenhower matrix")
    if not recommendations:
        recommendations.append("Great job maintaining balance! Keep up the healthy habits.")

    return {
        "stressRisk":      stress_risk,
        "burnoutRisk":     burnout_risk,
        "level":           level,
        "message":         message,
        "recommendations": recommendations
    }
