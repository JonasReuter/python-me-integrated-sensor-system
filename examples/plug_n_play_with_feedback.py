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

def simulated_sensor_stream():
    """
    Simuliert einen Sensor-Datenstream, der periodisch einen DataFrame mit 6D-Daten erzeugt.
    """
    while True:
        data = {
            "x": random.gauss(0, 1),
            "y": random.gauss(0, 1),
            "z": random.gauss(0, 1),
            "roll": random.gauss(0, 1),
            "pitch": random.gauss(0, 1),
            "yaw": random.gauss(0, 1)
        }
        # Simuliere in 10% der Fälle eine Anomalie
        if random.random() < 0.1:
            anomaly_field = random.choice(list(data.keys()))
            data[anomaly_field] += random.gauss(5, 1)
        yield pd.DataFrame([data])
        time.sleep(1)

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
                    # TODO: Verbesserung des Nutzerfeedbacks: Nicht-blockierende Eingabe bzw. asynchrone Abfrage implementieren.
                    feedback_input = input("Bestätigen Sie die Anomalie? (y/n): ").strip().lower()
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
                else:
                    print("Keine Anomalie im aktuellen Datenpaket.")
            else:
                time.sleep(self.polling_interval)

def main():
    logger = setup_logger("PlugNPlayFeedback", level=20)
    model = IsolationForestModel(contamination=0.05, n_estimators=10, random_state=42)
    # Dummy-Daten zur initialen Trainingsbasis
    dummy_data = pd.DataFrame({
        "x": [0]*100,
        "y": [0]*100,
        "z": [0]*100,
        "roll": [0]*100,
        "pitch": [0]*100,
        "yaw": [0]*100
    })
    model.train(dummy_data)
    
    # DB-Connector initialisieren (Beispiel: SQLite)
    db_url = "sqlite:///feedback.db"
    sql_connector = SQLConnector(db_url=db_url)
    
    feedback_engine = FeedbackInferenceEngine(model=model, polling_interval=1.0, db_connector=sql_connector)
    feedback_engine.start()

    # Periodischer Retraining-Zyklus (alle 5 Minuten)
    # TODO: Nach Retraining die Feedback-InferenceEngine mit dem neuen Modell updaten (z. B. durch Austausch von self.model).
    def retraining_loop():
        nonlocal model
        while True:
            model = online_learning_cycle(model, min_samples=10, epochs=3)
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
