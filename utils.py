def calculate_burnout_risk(study_hours, sleep_hours, deadlines):

    risk = 0

    if study_hours > 8:
        risk += 1

    if sleep_hours < 6:
        risk += 1

    if deadlines > 3:
        risk += 1

    if risk == 0:
        return "Low"

    elif risk == 1:
        return "Medium"

    else:
        return "High"