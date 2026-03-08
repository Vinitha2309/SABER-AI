def generate_plan(stress_score):

    if stress_score == 0:

        plan = {
            "Math": "2 hours",
            "Physics": "2 hours",
            "Programming": "2 hours"
        }

    elif stress_score == 1:

        plan = {
            "Math": "1 hour",
            "Physics": "1 hour",
            "Programming": "1 hour",
            "Break": "15 minutes",
            "Relaxation": "5 minutes breathing"
        }

    else:

        plan = {
            "Light Study": "30 minutes",
            "Break": "20 minutes",
            "Meditation": "10 minutes"
        }

    return plan