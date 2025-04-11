from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os
import uvicorn
import pandas as pd
from src.utils.config_utils import load_config

app = FastAPI(title="Integriertes System API")

# Konfiguration laden und Sensordimensionen bestimmen
config = load_config()
sensor_features = config["data"].get("sensor_features", ["x", "y", "z", "roll", "pitch", "yaw"])
sensor_units = config["data"].get("sensor_units", {})  # Neue: Einheiten der Sensoren
num_features = len(sensor_features)
api_config = config.get("api", {})  # Neue API-Konfiguration
api_host = api_config.get("host", "0.0.0.0")
api_port = api_config.get("port", 8000)

MODEL_PATH = config["model"].get("save_path", 
    os.path.join(os.path.dirname(__file__), "..", "anomaly_detection", "models", "isolation_forest_model.pkl"))

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
    # TODO: Weitere Validierungen bei Dummy-Daten und Modell-Initialisierung implementieren.
    dummy_data = pd.DataFrame({
        feat: [0]*100 for feat in sensor_features
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
        # Verwende num_features aus der Konfiguration
        features = np.zeros((1, num_features))
        prediction = model.predict(features)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host=api_host, port=api_port)
