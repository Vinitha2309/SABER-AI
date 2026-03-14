


# SABER-AI — Student Burnout Prevention & Adaptive Study Assistant

An **AI-powered web application** that helps students monitor stress, prevent burnout, and improve study efficiency through intelligent analysis of study habits, sleep patterns, and emotional states.

---

# 📌 Project Overview

**SABER-AI** is a full-stack web application designed to support student well-being and productivity.

The system analyzes:

* Study hours
* Sleep duration
* Mood/emotional state

Using this information, the application:

* Predicts **stress and burnout risk**
* Generates **adaptive study plans**
* Provides **emotion-aware recommendations**
* Tracks **student progress over time**

The goal is to help students maintain a **healthy balance between productivity and mental wellness**.

---

# ✨ Features

## 🧠 Stress Predictor

Analyzes **study hours, sleep hours, and mood** to calculate:

* Stress Risk (%)
* Burnout Risk (%)

Provides early warning when burnout risk is high.

---

## 📅 Adaptive Study Planner

Generates a **personalized study schedule** based on the student's stress level and available time.

The planner automatically adjusts:

* Session duration
* Break length
* Study intensity

---

## 🎤 Voice Emotion Detection

Detects the **student’s emotional state** and provides suitable study recommendations.

Possible emotions detected:

* Calm
* Focused
* Stressed
* Anxious
* Fatigued

---

## 📊 Dashboard

Displays important metrics including:

* Stress level
* Burnout risk
* Current emotion
* Study recommendations

Includes a **visual burnout gauge** using SVG and CSS animations.

---

## 📜 Session History

Stores previous sessions and allows students to:

* Track progress
* Observe stress patterns
* Review past recommendations

---

# 🛠️ Tech Stack

| Layer         | Technology            |
| ------------- | --------------------- |
| Frontend      | HTML, CSS, JavaScript |
| Backend       | Python, Flask         |
| API Support   | Flask-CORS            |
| Database      | SQLite                |
| Visualization | CSS Animations & SVG  |

---

# 📁 Project Structure

```
SABER-AI/
│
├── backend/
│   ├── app.py                # Main Flask API server
│   ├── database.py           # SQLite database connection and queries
│   ├── stress_model.py       # Stress and burnout prediction logic
│   ├── study_planner.py      # Adaptive study schedule generator
│   ├── voice_emotion.py      # Emotion detection logic
│   ├── requirements.txt      # Python dependencies
│   └── saber_ai.db           # SQLite database (auto created)
│
├── frontend/
│   ├── index.html            # Main web interface
│   ├── style.css             # UI styling and dark theme
│   └── script.js             # Frontend logic and API calls
│
├── start.bat                 # One-click startup script (Windows)
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/SABER-AI.git
cd SABER-AI
```

---

## 2️⃣ Install Dependencies

Navigate to the backend folder:

```
cd backend
pip install flask flask-cors
```

Or install using requirements file:

```
pip install -r requirements.txt
```

---

## 3️⃣ Start the Backend Server

```
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

---

## 4️⃣ Open the Frontend

Open the file:

```
frontend/index.html
```

You can open it:

* Directly in your browser
  OR
* Using **Live Server in VS Code**

---

# 🚀 Quick Start (Windows)

Simply **double click**:

```
start.bat
```

This script will automatically:

1. Start the backend server
2. Open the web application in your browser

---

# 🗄️ Database

The project uses **SQLite**, which requires **no manual setup**.

The database file:

```
saber_ai.db
```

is automatically created when the backend is started for the first time.

---

# 🧠 Stress Prediction Algorithm

Stress is calculated using a **scoring system** based on three factors.

---

## Study Hours Score

| Study Hours  | Score |
| ------------ | ----- |
| > 10 hours   | +40   |
| 7 – 10 hours | +20   |
| 5 – 7 hours  | +10   |

---

## Sleep Hours Score

| Sleep Hours | Score |
| ----------- | ----- |
| < 5 hours   | +40   |
| 5 – 6 hours | +25   |
| 6 – 7 hours | +10   |

---

## Mood Score

| Mood    | Score |
| ------- | ----- |
| Happy   | +0    |
| Neutral | +10   |
| Sad     | +25   |
| Angry   | +30   |
| Anxious | +35   |

---

## Final Calculation

```
Stress Risk = Total Score
Burnout Risk = Stress Risk × 0.9
```

---

# 📊 Study Planner Logic

The planner adjusts study sessions depending on stress level.

| Stress Level    | Session | Break  | Intensity |
| --------------- | ------- | ------ | --------- |
| High (70%+)     | 25 min  | 10 min | Light     |
| Medium (40-70%) | 35 min  | 8 min  | Moderate  |
| Low (<40%)      | 50 min  | 10 min | Focused   |

---

# 🎭 Emotion Detection

Voice emotion analysis identifies the user's emotional state and provides recommendations.

| Emotion  | Recommendation                  |
| -------- | ------------------------------- |
| Calm     | Ideal for focused studying      |
| Focused  | Suitable for difficult subjects |
| Stressed | Suggests short breaks           |
| Anxious  | Recommends light exercise       |
| Fatigued | Advises rest before studying    |

---

# 👩‍💻 Development Mode

Run the backend with auto-reload:

```
cd backend
python app.py
```

Flask runs with:

```
debug=True
```

This automatically reloads the server when code changes.

---

# 📄 License

This project is created **for educational purposes** as part of an **AI-Powered Student Assistance System**.

---

# 🙌 Acknowledgements

Built using:

* Flask
* SQLite
* Vanilla JavaScript

Designed with a **dark professional interface** focused on **student productivity and mental wellness**.

