from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os
import uvicorn

app = FastAPI(title="Integriertes System API")

# Angenommener Pfad zum trainierten Isolation-Forest-Modell, das mittels joblib gespeichert wurde
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "anomaly_detection", "models", "isolation_forest_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Fehler beim Laden des Modells: {e}")

class PredictRequest(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "Anomaly Detection API is running."}

@app.post("/predict")
def predict(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Modell nicht verfügbar. Bitte trainiere zuerst das Modell.")
    try:
        # Eingabedaten in ein 2D NumPy-Array umformen
        features = np.array(request.features).reshape(1, -1)
        # Isolation-Forest liefert -1 als Anomalie und 1 als normal
        prediction = model.predict(features)
        anomaly = True if prediction[0] == -1 else False
        # Entscheidungsscore liefert einen Wert, der näher an negativen Werten bei Anomalien liegt
        anomaly_score = float(model.decision_function(features)[0])
        return {
            "anomaly": anomaly,
            "anomaly_score": anomaly_score
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
