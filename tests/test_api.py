import unittest
from fastapi.testclient import TestClient
from src.api.main_api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Willkommen", response.json()["message"])

    def test_predict(self):
        response = self.client.get("/predict")
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())

if __name__ == '__main__':
    unittest.main()
