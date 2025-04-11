import time
import random
import pandas as pd

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

def detect_anomaly(df: pd.DataFrame, threshold: float = 3.0):
    """
    Erkennt eine Anomalie, wenn irgendein Sensordatenwert den Schwellenwert überschreitet.
    """
    for col in df.columns:
        if abs(df[col].iloc[0]) > threshold:
            return True, col, df[col].iloc[0]
    return False, None, None

def simple_anomaly_detection():
    print("Starte einfache Anomalie-Erkennung bei generierten Sensordaten...")
    for _ in range(20):
        data = generate_sensor_data()
        anomaly, feature, value = detect_anomaly(data)
        print("Sensordaten:", data.to_dict(orient="records")[0])
        if anomaly:
            print(f"Anomalie erkannt: {feature} = {value:.2f}")
        else:
            print("Keine Anomalie erkannt.")
        time.sleep(1) 
    print("Einfache Anomalie-Erkennung beendet.")

if __name__ == '__main__':
    simple_anomaly_detection()
