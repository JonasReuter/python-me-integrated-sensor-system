import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import threading
import time
from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
from src.utils.logging_utils import setup_logger
from src.data_integration.db_connector.sql_connector import SQLConnector

from examples.plug_n_play_with_feedback import (
    main,
    simulated_sensor_stream,
    FeedbackInferenceEngine
)

class DummyModel:
    def predict(self, data):
        # Always return anomaly
        return np.array([-1])
    def train(self, data):
        pass

class DummyDBConnector:
    def __init__(self):
        self.saved = []
    def save_feedback(self, sample):
        self.saved.append(sample)

def finite_sensor_stream():
    # Yield one sensor reading and then stop.
    data = {
        "x": 0.5,
        "y": -0.2,
        "z": 0.1,
        "roll": 0.0,
        "pitch": 0.0,
        "yaw": 0.0
    }
    yield pd.DataFrame([data])

class TestSimulatedSensorStream(unittest.TestCase):
    def test_stream_yields_dataframe(self):
        stream = simulated_sensor_stream()
        with patch('time.sleep', return_value=None):
            df = next(stream)
        self.assertTrue(isinstance(df, pd.DataFrame))
        for col in ["x", "y", "z", "roll", "pitch", "yaw"]:
            self.assertIn(col, df.columns)

class TestFeedbackInferenceEngine(unittest.TestCase):
    @patch("builtins.input", return_value="y")
    def test_process_data_calls_db_save(self, mock_input):
        data = pd.DataFrame([{
            "x": 1.0, "y": 1.0, "z": 1.0, "roll": 1.0, "pitch": 1.0, "yaw": 1.0
        }])
        dummy_model = DummyModel()
        dummy_db = DummyDBConnector()
        engine = FeedbackInferenceEngine(model=dummy_model, polling_interval=0.1, db_connector=dummy_db)
        engine.data_queue.put(data)
        def run_once():
            engine._process_data()
            engine.is_running = False
        engine.is_running = True
        t = threading.Thread(target=run_once)
        t.start()
        t.join(timeout=1)
        self.assertGreater(len(dummy_db.saved), 0)
        saved_sample = dummy_db.saved[0]
        self.assertIn("prediction", saved_sample)
        self.assertIn("feedback", saved_sample)

class TestMainFunction(unittest.TestCase):
    @patch("examples.plug_n_play_with_feedback.simulated_sensor_stream", side_effect=finite_sensor_stream)
    @patch("time.sleep", return_value=None)
    @patch("builtins.input", return_value="y")
    def test_main_runs_once(self, mock_input, mock_sleep, mock_stream):
        with patch.object(FeedbackInferenceEngine, "start", return_value=None) as mock_start, \
             patch.object(FeedbackInferenceEngine, "stop", return_value=None) as mock_stop, \
             patch("examples.plug_n_play_with_feedback.online_learning_cycle", lambda model, **kwargs: model):
            def run_main():
                try:
                    main()
                except Exception:
                    pass
            t = threading.Thread(target=run_main)
            t.start()
            time.sleep(0.2)
            t.join(timeout=1)
            mock_start.assert_called_once()
            mock_stop.assert_called_once()

if __name__ == '__main__':
    unittest.main()