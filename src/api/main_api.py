from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os
import uvicorn
import pandas as pd

app = FastAPI(title="Integriertes System API")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "anomaly_detection", "models", "isolation_forest_model.pkl")

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
    # TODO: Weitere Validierungen bei Dummy-Daten und Modell-Initialisierung implementieren.
    dummy_data = pd.DataFrame({
        "x": [0]*100,
        "y": [0]*100,
        "z": [0]*100,
        "roll": [0]*100,
        "pitch": [0]*100,
        "yaw": [0]*100
    })
    model = IsolationForestModel(contamination=0.05, n_estimators=100, random_state=42)
    model.train(dummy_data)
    joblib.dump(model, MODEL_PATH)

class PredictRequest(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "Willkommen bei der Anomaly Detection API."}

@app.get("/predict")
def predict():
    if model is None:
        raise HTTPException(status_code=500, detail="Modell nicht verfügbar. Bitte trainiere zuerst das Modell.")
    try:
        # TODO: Möglichkeit zum direkten Aufruf mit spezifischen Features implementieren.
        features = np.zeros((1, 6))
        prediction = model.predict(features)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
