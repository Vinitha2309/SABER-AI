import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

model_file = "stress_model.pkl"

def train_model():

    data = pd.read_csv("../dataset/sample_student_data.csv")

    X = data[['study_hours','sleep_hours','deadlines','typing_speed']]
    y = data['stress_level']

    model = RandomForestClassifier()
    model.fit(X,y)

    joblib.dump(model, model_file)

def load_model():

    if not os.path.exists(model_file):
        train_model()

    return joblib.load(model_file)

def predict_stress(study,sleep,deadlines,typing):

    model = load_model()

    prediction = model.predict([[study,sleep,deadlines,typing]])

    return int(prediction[0])
