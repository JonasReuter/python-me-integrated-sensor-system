import unittest
import pandas as pd
import numpy as np
from src.data_processing.transformer import clean_data, normalize_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "A": np.arange(10),
            "B": np.linspace(0, 1, 10)
        })

    def test_clean_data(self):
        cleaned = clean_data(self.data)
        self.assertEqual(cleaned.shape[0] <= self.data.shape[0], True)

    def test_normalize_data(self):
        normalized = normalize_data(self.data)
        self.assertTrue((normalized.max().max() <= 1))
        self.assertTrue((normalized.min().min() >= 0))

if __name__ == '__main__':
    unittest.main()
