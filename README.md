 SABER-AI — Student Burnout Prevention & Adaptive Study Assistant

An AI-powered web application that helps students prevent burnout by predicting stress levels, generating personalized study plans, and detecting emotional states.

---

📌 Project Overview

SABER-AI is a full-stack web application built for students to monitor their mental health and academic performance. It uses intelligent algorithms to analyze study patterns, sleep habits, and mood to predict burnout risk and provide actionable recommendations.

---

✨ Features

| Feature & Description |

|Stress Predictor | Analyzes study hours, sleep, and mood to calculate stress and burnout risk |,
| Adaptive Study Planner |Generates a personalized study schedule based on your stress level and available time |,
| Voice Emotion Detection | Detects your emotional state and provides study recommendations |,
| Session History |Tracks all your past sessions and shows progress over time |,
| Dashboard | Displays your latest stats with visual burnout gauge |.

---
 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask, Flask-CORS |
| Database | SQLite (saber_ai.db) |
| Charts | CSS animations and SVG gauge |

---


## 📁 Project Structure
SABER-AI/
├── backend/│
├── database.py ← SQLite database connection and queries
│ ├── stress_model.py ← Stress and burnout prediction algorithm
│ ├── study_planner.py ← Adaptive study schedule generator
│ ├── voice_emotion.py ← Emotion detection logic
│ ├── requirements.txt ← Python dependencies
│ └── saber_ai.db ← SQLite database (auto-created on first run)
├── frontend/
│ ├── index.html ← Main HTML page
│ ├── style.css ← All styles and dark theme
│ └── script.js ← Frontend logic and API calls
├── start.bat ← One-click startup script (Windows)
└── README.md ← This file

---
## ⚙️ Installation and Setup
Step 1:
cd SABER-AI-main\backend
pip install flask flask-cors
Step 2 — Start the Backend
python app.py
You should see:

* Running on http://127.0.0.1:5000
* Press CTRL+C to quit
Step 4 — Open the Frontend
Open frontend/index.html in your browser directly, or use Live Server in VS Code.

🚀 Quick Start (Windows)
Double click start.bat in the main folder. It automatically starts the backend and opens the app in your browser.

🔌 API Endpoints
Method	Endpoint	Description
POST	/api/predict-stress	Predicts stress and burnout risk
POST	/api/generate-plan	Generates an adaptive study schedule
POST	/api/detect-emotion	Detects current emotional state
GET	/api/sessions	Retrieves all saved sessions
POST	/api/sessions	Saves a new session

🗄️ Database
The project uses SQLite — no setup required. The database file saber_ai.db is created automatically when you first run python app.py.

Sessions Table Schema
Column	Type	Description
id	INTEGER	Auto-increment primary key
study_hours	REAL	Hours studied per day
sleep_hours	REAL	Hours slept last night
mood	TEXT	Current mood (happy, neutral, sad, anxious, angry)
stress_risk	REAL	Predicted stress risk percentage
burnout_risk	REAL	Predicted burnout risk percentage
emotion	TEXT	Detected emotion from voice analysis
created_at	TEXT	Timestamp of the session

🧠 How the Stress Algorithm Works
The stress prediction uses a scoring system based on three factors:

Study Hours Score:

More than 10 hours → +40 points,
7 to 10 hours → +20 points,
5 to 7 hours → +10 points.

Sleep Hours Score:

Less than 5 hours → +40 points,
5 to 6 hours → +25 points,
6 to 7 hours → +10 points.

Mood Score:

Happy → +0 points
Neutral → +10 points
Sad → +25 points
Anxious → +35 points
Angry → +30 points
Total score = Stress Risk %. Burnout Risk = Stress Risk × 0.9

📊 Study Planner Logic
The planner adjusts session duration based on your stress level:

Stress Level	Session Duration	Break	Intensity
High (70%+)	25 minutes	10 min	Light
Medium (40-70%)	35 minutes	8 min	Moderate
Low (under 40%)	50 minutes	10 min	Focused

🎭 Emotion Detection
The Voice Emotion feature analyzes your current state and returns one of five emotions:

Calm — Great for focused study,
Focused — Perfect for difficult subjects,
Stressed — Recommends short breaks,
Anxious — Recommends light exercise first,
Fatigued — Recommends rest before studying.


👩‍💻 Development
To run in development mode with auto-reload:

cd backend
python app.py
The backend runs with debug=True by default which auto-reloads when you change Python files.

📄 License
This project is created for educational purposes as part of an AI-Powered Student Assistance System.

🙌 Acknowledgements
Built with Flask, SQLite, and vanilla JavaScript. Designed with a dark professional theme focused on student wellness and academic performance.


