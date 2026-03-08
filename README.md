 SABER-AI

AI-Powered Predictive Burnout Prevention and Adaptive Study Assistant for Students

 📌 Project Overview

SABER-AI is an intelligent system designed to detect and prevent academic burnout among students.
The system analyzes study behavior, sleep patterns, deadlines, and typing speed to predict stress levels using machine learning.

It also adapts study plans dynamically and detects emotional stress from voice input to support student well-being and productivity.

🎯 Problem Statement

Students often face high academic pressure due to exams, assignments, and continuous digital learning.
Most productivity tools only track study time and fail to detect early signs of stress or burnout.

SABER-AI solves this problem by predicting stress early and providing adaptive study recommendations to help students maintain a healthy study routine.


🚀 Features

* 📊 **Stress Prediction System**
  Predicts student stress levels based on behavioral data.

* 📅 **Exam Stress Forecasting**
  Identifies potential stress before exams.

* 🧠 **AI Adaptive Study Planner**
  Automatically adjusts study schedules according to stress levels.

* 🎤 **Voice Emotion Detection**
  Detects stress, calmness, or neutral emotions from voice input.

* 📉 **Burnout Risk Monitoring**
  Calculates burnout risk based on study habits and sleep patterns.

* 📋 **Smart Study Recommendations**
  Provides personalized suggestions for better study balance.



 🛠️ Technologies Used

**Backend**

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Librosa (Voice Processing)

**Frontend**

* HTML
* CSS
* JavaScript

**Machine Learning**

* Random Forest Classifier

---

### 📂 Project Structure

```
SABER-AI
│
├── backend
│   ├── app.py
│   ├── stress_model.py
│   ├── study_planner.py
│   ├── voice_emotion.py
│   ├── utils.py
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── dataset
│   └── sample_student_data.csv
│
└── README.md
```

---

⚙️ Installation

1. Clone the repository


git clone https://github.com/yourusername/SABER-AI.git
```

2. Navigate to backend folder

```
cd SABER-AI/backend
```

3. Install required libraries

```
pip install -r requirements.txt
```

---

### ▶️ Running the Project

Start the backend server:

```
python app.py
```

The server will start at:


http://127.0.0.1:5000


Open the frontend by launching:

```
frontend/index.html
```

in your browser.

---

📊 Example Input

| Study Hours | Sleep Hours | Deadlines | Typing Speed |
| ----------- | ----------- | --------- | ------------ |
| 8           | 5           | 3         | 40 WPM       |

Example Output:

```
Stress Level: Medium
Recommended Plan:
Math – 1 hour
Physics – 1 hour
Programming – 1 hour
Break – 15 minutes
Relaxation – 5 minutes
```


🌟 Future Improvements

* Mobile application version
* Real-time typing behavior analysis
* Integration with wearable health devices
* Advanced deep learning emotion detection
* Student mental health analytics dashboard

---

 👩‍💻 Author

Vinitha Y


📜 License

This project is developed for academic and educational purposes.
