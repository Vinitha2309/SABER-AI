def generate_plan(stress_level, available_hours, subjects):
    if not subjects:
        subjects = ["General Study"]

    if stress_level >= 70:
        session_duration = 25
        break_duration   = 10
        intensity        = "Light"
    elif stress_level >= 40:
        session_duration = 35
        break_duration   = 8
        intensity        = "Moderate"
    else:
        session_duration = 50
        break_duration   = 10
        intensity        = "Focused"

    schedule   = []
    total_mins = int(float(available_hours) * 60)
    used_mins  = 0
    slot_num   = 1
    sub_index  = 0

    while used_mins + session_duration <= total_mins:
        subject    = subjects[sub_index % len(subjects)]
        start_hour = 8 + (used_mins // 60)
        start_min  = used_mins % 60
        end_mins   = used_mins + session_duration
        end_hour   = 8 + (end_mins // 60)
        end_min    = end_mins % 60

        schedule.append({
            "slot":     slot_num,
            "subject":  subject,
            "duration": session_duration,
            "start":    f"{start_hour:02d}:{start_min:02d}",
            "end":      f"{end_hour:02d}:{end_min:02d}",
            "type":     intensity
        })

        used_mins += session_duration + break_duration
        slot_num  += 1
        sub_index += 1

    return {
        "schedule":        schedule,
        "totalSessions":   len(schedule),
        "totalStudyTime":  len(schedule) * session_duration,
        "sessionDuration": session_duration,
        "breakDuration":   break_duration,
        "intensity":       intensity,
        "recommendation":  get_recommendation(stress_level)
    }


def get_recommendation(stress_level):
    if stress_level >= 70:
        return "High stress detected. Take frequent breaks and avoid late-night studying."
    elif stress_level >= 40:
        return "Moderate stress. Keep a balanced schedule with short breaks."
    else:
        return "Low stress. Great time for deep focused study sessions!"
