#!/usr/bin/env python3
"""
Plug n Play Script mit adaptiver Feedback-Engine und DB-Anbindung.

Dieses Script simuliert einen Livestream von 6D-Sensordaten, erkennt Anomalien,
fragt das Nutzerfeedback ("y" für bestätigte Anomalie, "n" für False Positive) ab und
speichert das Feedback in der Datenbank. Zusätzlich wird ein periodischer Retraining-Zyklus gestartet,
der die gesammelten Feedbackdaten zur Modellverbesserung nutzt.

Voraussetzungen: 
- Der SQLConnector speichert Feedback in einer Datenbank (z.B. SQLite).
- Die GSV-Integration (falls verwendet) wird ebenfalls angesprochen, siehe src/gsv_integration/.
"""

import time
import threading
import random
import pandas as pd
from src.realtime_inference.inference_engine import InferenceEngine
from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
from src.utils.logging_utils import setup_logger
from src.data_integration.db_connector.sql_connector import SQLConnector
from src.online_learning.online_learning import online_learning_cycle
from src.utils.config_utils import load_config

# Konfiguration laden
config = load_config()
sensor_features = config["data"].get("sensor_features", ["x", "y", "z", "roll", "pitch", "yaw"])
sensor_units = config["data"].get("sensor_units", {})  # Neue: Einheiten der Sensoren

def simulated_sensor_stream():
    """
    Simuliert einen Sensor-Datenstream mit Einheiten (zur internen Verwendung).
    """
    while True:
        data = { feature: random.gauss(0, 1) for feature in sensor_features }
        # Simuliere in 10% der Fälle eine Anomalie
        if random.random() < 0.1:
            anomaly_field = random.choice(sensor_features)
            data[anomaly_field] += random.gauss(5, 1)
        # Optional: Anzeige der Sensorwerte mit Einheiten (nur zur Demonstration)
        # data_with_units = { feature: f"{value} {sensor_units.get(feature, '')}" for feature, value in data.items() }
        yield pd.DataFrame([data])
        time.sleep(1)

def get_nonblocking_feedback(prompt: str, timeout: float = 5.0) -> str:
    import threading
    result = []
    def target():
        result.append(input(prompt))
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        return None
    return result[0].strip().lower() if result else None

class FeedbackInferenceEngine(InferenceEngine):
    def __init__(self, model, polling_interval: float = 0.5, db_connector=None):
        super().__init__(model, polling_interval)
        self.db_connector = db_connector
    
    def _process_data(self):
        while self.is_running:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                predictions = self.model.predict(data)
                if any(pred == -1 for pred in predictions):
                    print("\nAnomalie erkannt in den folgenden Sensordaten:")
                    print(data)
                    # Nicht-blockierende Abfrage des Nutzerfeedbacks
                    feedback_input = get_nonblocking_feedback("Bestätigen Sie die Anomalie? (y/n): ", timeout=5)
                    feedback_input = feedback_input if feedback_input is not None else "n"
                    feedback_label = 1 if feedback_input == 'y' else 0
                    # Erstellen eines Feedback-Datensatzes
                    sample = data.iloc[0].to_dict()
                    sample.update({"prediction": -1, "feedback": feedback_label})
                    print("Feedback: ", "Anomalie bestätigt." if feedback_label == 1 else "False Positive.")
                    if self.db_connector:
                        try:
                            self.db_connector.save_feedback(sample)
                            print("Feedback in Datenbank gespeichert.")
                        except Exception as e:
                            print("Fehler beim Speichern in der DB:", e)
                    # TODO: Eventuell weitere Aktionen (z. B. lokale Speicherung oder alternative Persistenz) implementieren.
                else:
                    print("Keine Anomalie im aktuellen Datenpaket.")
            else:
                time.sleep(self.polling_interval)

def main():
    logger = setup_logger("PlugNPlayFeedback", level=20)
    model = IsolationForestModel(contamination=0.05, n_estimators=10, random_state=42)
    # Dummy-Daten zur initialen Trainingsbasis
    dummy_data = pd.DataFrame({
        feat: [0]*100 for feat in sensor_features
    })
    model.train(dummy_data)
    
    # NEU: Prüfe, ob eine Excel-Datei in data/raw existiert und verarbeite diese
    import os
    excel_path = os.path.join("data", "raw", "sensordata.xlsx")
    if os.path.exists(excel_path):
        print("Excel Datei gefunden. Verarbeite 6D Sensordaten aus:", excel_path)
        # Falls in der Excel-Datei das Komma als Dezimaltrennzeichen verwendet wird:
        df_excel = pd.read_excel(excel_path, decimal=",")
        # Optional: Falls kein Header in der Excel-Datei vorhanden ist, setzen Sie diesen manuell.
        # Beispiel: Es werden die ersten 6 Spalten als Sensorwerte angenommen.
        if df_excel.columns.tolist()[0] != sensor_features[0]:
            df_excel.columns = sensor_features + list(df_excel.columns[6:])
        # Wählen Sie nur die Spalten, die den Sensordaten entsprechen
        df_sensor = df_excel[sensor_features]
        predictions = model.predict(df_sensor)
        print("Vorhersagen aus der Excel-Datei:", predictions)
        # Optional: Den Prozess hier beenden, wenn nur die Excel-Daten getestet werden sollen.
        return
    
    # DB-Connector initialisieren (Beispiel: SQLite)
    db_url = "sqlite:///feedback.db"
    sql_connector = SQLConnector(db_url=db_url)
    
    feedback_engine = FeedbackInferenceEngine(model=model, polling_interval=1.0, db_connector=sql_connector)
    feedback_engine.start()

    # Periodischer Retraining-Zyklus (alle 5 Minuten)
    def retraining_loop():
        nonlocal model
        while True:
            model = online_learning_cycle(model, min_samples=10, epochs=3)
            feedback_engine.model = model  # neues Modell wird der Engine zugewiesen
            time.sleep(300)
    retraining_thread = threading.Thread(target=retraining_loop, daemon=True)
    retraining_thread.start()

    try:
        for sensor_data in simulated_sensor_stream():
            feedback_engine.add_data(sensor_data)
    except KeyboardInterrupt:
        print("Livestream wird beendet...")
    finally:
        feedback_engine.stop()

if __name__ == '__main__':
    main()
