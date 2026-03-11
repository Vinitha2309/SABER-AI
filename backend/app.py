from flask import Flask, request, jsonify
from stress_model import predict_stress
from study_planner import generate_plan
from voice_emotion import detect_emotion

app = Flask(__name__)

@app.route('/')
def home():
    return "SABER-AI Backend Running"

@app.route("/predict_stress", methods=["POST"])
def stress():

    data = request.json

    study = float(data["study_hours"])
    sleep = float(data["sleep_hours"])
    deadlines = float(data["deadlines"])
    typing = float(data["typing_speed"])

    result = predict_stress(study, sleep, deadlines, typing)

    plan = generate_plan(result)

    return jsonify({
        "stress_level": int(result),
        "recommended_plan": plan
    })


@app.route("/voice_emotion", methods=["POST"])
def voice():

    file = request.files["file"]

    emotion = detect_emotion(file)

    return jsonify({
        "emotion": emotion
    })


if __name__ == "__main__":
    app.run(debug=True)
