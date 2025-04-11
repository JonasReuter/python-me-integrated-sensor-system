import time
import random
import threading
import pandas as pd
from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel

def simulate_sensor_data():
    """
    Simuliert Sensordaten für einen erweiterten Predictive Maintenance Use-Case.
    Es werden 6D-Kraftsensor-Messwerte (Fx, Fy, Fz, Mx, My, Mz) sowie zusätzliche Parameter 
    wie temperature, vibration und pressure generiert.
    # Hinweis: In einer realen Anwendung ersetzen Sie diese Zufallsdaten durch echte Sensordaten.
    # Beispielweise können Sie hier Daten von einer industriellen Sensor-Schnittstelle, einem REST-API-Endpunkt
    # oder aus einem direkten Datenbankzugriff abrufen.
    """
    while True:
        data = {
            # 6D-Kraftsensor-Daten (Simulation)
            "Fx": round(random.uniform(0, 100), 2),
            "Fy": round(random.uniform(0, 100), 2),
            "Fz": round(random.uniform(0, 100), 2),
            "Mx": round(random.uniform(0, 20), 2),
            "My": round(random.uniform(0, 20), 2),
            "Mz": round(random.uniform(0, 20), 2),
            # Zusätzliche Sensorwerte (Simulation)
            "temperature": round(random.uniform(20, 100), 2),
            "vibration": round(random.uniform(0, 10), 2),
            "pressure": round(random.uniform(1, 5), 2)
        }
        yield pd.DataFrame([data])
        time.sleep(2)

def stop_machine():
    """
    Simuliert das Senden des Stop-Befehls an eine Maschine.
    # Hinweis: Für den Echtbetrieb würden Sie an dieser Stelle eine API oder ein Protokoll zur Steuerung der Maschine 
    # implementieren (z. B. über OPC-UA, MQTT oder proprietäre Schnittstellen).
    """
    print("Maschine wird gestoppt! [FERTIGER PREDICTIVE MAINTENANCE FALL]")

def process_data(df: pd.DataFrame, model):
    data = df.iloc[0].to_dict()
    # Modellbasierte Anomalieerkennung: -1 signalisiert eine Anomalie
    prediction = model.predict(df)
    if prediction[0] == -1:
        print("Anomalie erkannt durch Modell. Sensordaten:", data)
        stop_machine()
    else:
        print("Betrieb normal. Sensordaten:", data)

def maintenance_case(model):
    print("Starte erweiterten Predictive Maintenance Fall (Modell-basierte Anomalieerkennung)...")
    for sensor_data in simulate_sensor_data():
        process_data(sensor_data, model)

if __name__ == '__main__':
    # Modell initialisieren und Dummy-Trainingsdaten erstellen
    features = ["Fx", "Fy", "Fz", "Mx", "My", "Mz", "temperature", "vibration", "pressure"]
    dummy_data = pd.DataFrame({
        feat: [random.uniform(0, 100) if feat in ["Fx", "Fy", "Fz", "temperature"] 
               else random.uniform(0, 20) if feat in ["Mx", "My", "Mz"] 
               else random.uniform(0, 10) if feat == "vibration" 
               else random.uniform(1, 5)
               for _ in range(100)]
        for feat in features
    })
    model = IsolationForestModel(contamination=0.05, n_estimators=100, random_state=42)
    model.train(dummy_data)
    # Hinweis: Im Produktionsumfeld würden Sie das Modell mit echten Trainingsdaten trainieren 
    # bzw. ein bereits vorab trainiertes Modell laden.
    maintenance_thread = threading.Thread(target=lambda: maintenance_case(model))
    maintenance_thread.start()
    time.sleep(30)  # Beispiel-Laufzeit 30 Sekunden
    print("Predictive Maintenance Fall beendet.")
