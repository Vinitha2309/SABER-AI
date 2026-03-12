from flask import Flask, request, jsonify
from flask_cors import CORS
from stress_model import predict_stress
from study_planner import generate_plan
from voice_emotion import detect_emotion
from database import save_session, get_sessions

app = Flask(__name__)
CORS(app)

# ── Stress Prediction ──────────────────────────────────────────
@app.route("/api/predict-stress", methods=["POST"])
def stress():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required = ["studyHours", "sleepHours", "mood"]
    if not all(k in data for k in required):
        return jsonify({"error": f"Missing fields: {required}"}), 400

    result = predict_stress(
        study_hours=float(data["studyHours"]),
        sleep_hours=float(data["sleepHours"]),
        mood=data["mood"],
        assignments_due=int(data.get("assignmentsDue", 0)),
        exercise_minutes=int(data.get("exerciseMinutes", 0))
    )
    return jsonify(result)


# ── Study Planner ──────────────────────────────────────────────
@app.route("/api/study-plan", methods=["POST"])
def study():
    data = request.get_json()
    if not data or "stressLevel" not in data:
        return jsonify({"error": "stressLevel is required"}), 400

    plan = generate_plan(
        stress_level=float(data["stressLevel"]),
        subjects=data.get("subjects", []),
        available_hours=float(data.get("availableHours", 6))
    )
    return jsonify(plan)


# ── Voice Emotion Detection ────────────────────────────────────
@app.route("/api/detect-emotion", methods=["POST"])
def emotion():
    result = detect_emotion()
    return jsonify(result)


# ── Save Session ───────────────────────────────────────────────
@app.route("/api/sessions", methods=["POST"])
def save():
    data = request.get_json()
    required = ["studyHours", "sleepHours", "mood", "stressRisk", "burnoutRisk"]
    if not data or not all(k in data for k in required):
        return jsonify({"error": f"Missing fields: {required}"}), 400

    session = save_session(data)
    return jsonify(session), 201


# ── Get All Sessions ───────────────────────────────────────────
@app.route("/api/sessions", methods=["GET"])
def sessions():
    return jsonify(get_sessions())


# ── Health Check ───────────────────────────────────────────────
@app.route("/api/healthz", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)


