import joblib
from sklearn.ensemble import RandomForestClassifier
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "rf_model.pkl")
    if not os.path.exists(model_path):
        model = RandomForestClassifier()
        model.fit([[10,1,2,3.0,300]], [0])  # dummy train
        joblib.dump(model, model_path)
    return joblib.load(model_path)
