import librosa
import numpy as np
import soundfile as sf
import tempfile

def extract_features(file_path):

    audio, sr = librosa.load(file_path)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

    return np.mean(mfcc.T, axis=0)


def detect_emotion(file):

    with tempfile.NamedTemporaryFile(delete=False) as temp:

        file.save(temp.name)

        features = extract_features(temp.name)

        score = np.mean(features)

        if score > -200:
            emotion = "Stress"
        elif score > -300:
            emotion = "Neutral"
        else:
            emotion = "Calm"

    return emotion