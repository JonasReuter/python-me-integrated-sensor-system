import unittest
import pandas as pd
import numpy as np
from src.visualization.pairplot import create_pairplot

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "X": np.random.randn(50),
            "Y": np.random.randn(50),
            "Z": np.random.randn(50)
        })

    def test_pairplot(self):
        # Testet, ob die Funktion ohne Fehler durchläuft
        create_pairplot(self.data, title="Test Pairplot")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
