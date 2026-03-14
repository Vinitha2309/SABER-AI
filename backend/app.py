from flask import Flask, request, jsonify
from flask_cors import CORS
from stress_model import predict_stress
from study_plan import generate_plan
from voice_emotion import detect_emotion
from database import save_session, get_sessions

app = Flask(__name__)
CORS(app)


@app.route("/api/predict-stress", methods=["POST"])
def stress():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        result = predict_stress(
            study_hours = float(data.get("studyHours", 0)),
            sleep_hours = float(data.get("sleepHours", 0)),
            mood        = data.get("mood", "neutral")
        )
        save_session({
            "studyHours":  data.get("studyHours", 0),
            "sleepHours":  data.get("sleepHours", 0),
            "mood":        data.get("mood", "neutral"),
            "stressRisk":  result["stressRisk"],
            "burnoutRisk": result["burnoutRisk"],
            "emotion":     None
        })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/generate-plan", methods=["POST"])
def plan():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        stress_level    = float(data.get("stressLevel",    50))
        available_hours = float(data.get("availableHours",  4))
        subjects        = data.get("subjects", ["General Study"])

        if isinstance(subjects, str):
            subjects = [s.strip() for s in subjects.split(",") if s.strip()]
        if not subjects:
            subjects = ["General Study"]

        result = generate_plan(stress_level, available_hours, subjects)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/detect-emotion", methods=["POST"])
def emotion():
    data   = request.get_json() or {}
    result = detect_emotion(data.get("text", ""))
    return jsonify(result), 200


@app.route("/api/sessions", methods=["GET"])
def sessions_get():
    try:
        return jsonify(get_sessions()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/sessions", methods=["POST"])
def sessions_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    try:
        result = save_session(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
