from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Integriertes System API")

@app.get("/")
def read_root():
    return {"message": "Willkommen beim Integrierten System API"}

@app.get("/predict")
def predict():
    # Dummy-Vorhersage; in einem realen Szenario hier Modellinferenz integrieren
    return {"prediction": [1, -1, 1]}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
