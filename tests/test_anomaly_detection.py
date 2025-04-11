import unittest
import pandas as pd
import numpy as np
from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
from src.anomaly_detection.models.autoencoder_model import AutoencoderModel

class TestAnomalyDetection(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(np.random.normal(0, 1, size=(100, 6)), columns=["x", "y", "z", "roll", "pitch", "yaw"])

    def test_isolation_forest(self):
        model = IsolationForestModel(contamination=0.05, n_estimators=10, random_state=42)
        model.train(self.data)
        predictions = model.predict(self.data)
        self.assertTrue(set(predictions).issubset({-1, 1}))

    def test_autoencoder(self):
        input_dim = self.data.shape[1]
        model = AutoencoderModel(input_dim=input_dim, encoding_dim=3, epochs=1, batch_size=10)
        model.train(self.data)
        errors = model.predict(self.data)
        self.assertEqual(len(errors), self.data.shape[0])
        self.assertTrue(np.all(np.isfinite(errors)))

if __name__ == '__main__':
    unittest.main()
