import time
import random
import pandas as pd
from sklearn.ensemble import IsolationForest

def generate_sensor_data():
    """
    Generiert Sensordaten mit normalverteilten Werten.
    In 15% der Fälle wird ein Anomaliewert hinzugefügt.
    """
    data = {
        "x": random.gauss(0, 1),
        "y": random.gauss(0, 1),
        "z": random.gauss(0, 1),
        "roll": random.gauss(0, 1),
        "pitch": random.gauss(0, 1),
        "yaw": random.gauss(0, 1)
    }
    if random.random() < 0.15:
        anomaly_feature = random.choice(list(data.keys()))
        data[anomaly_feature] += random.uniform(4, 6)
    return pd.DataFrame([data])

def detect_anomaly(df: pd.DataFrame, model: IsolationForest):
    """
    Nutzt IsolationForest um Anomalien zu erkennen.
    """
    pred = model.predict(df)
    score = model.decision_function(df)
    if pred[0] == -1:
        return True, score[0]
    return False, score[0]

def simple_anomaly_detection():
    print("Trainiere Isolation Model auf Basis von generierten Sensordaten...")
    # Generiere Trainingsdaten (100 Samples)
    training_data = pd.concat([generate_sensor_data() for _ in range(100)], ignore_index=True)
    model = IsolationForest(contamination=0.15, random_state=42)
    model.fit(training_data)
    print("Isolation Model trainiert. Starte Anomalie-Erkennung bei neuen Sensordaten...")
    
    for _ in range(20):
        data = generate_sensor_data()
        anomaly, score = detect_anomaly(data, model)
        print("Sensordaten:", data.to_dict(orient="records")[0])
        if anomaly:
            print(f"Anomalie erkannt (score={score:.2f}).")
        else:
            print("Keine Anomalie erkannt.")
        time.sleep(1) 
    print("Anomalie-Erkennung beendet.")

if __name__ == '__main__':
    simple_anomaly_detection()
