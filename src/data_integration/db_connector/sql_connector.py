import sqlite3
import pandas as pd

class SQLConnector:
    def __init__(self, db_url):
        # Extrahiere den Dateipfad aus der URL (z. B. "sqlite:///feedback.db")
        db_path = db_url.split(":///")[-1]
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                x REAL,
                y REAL,
                z REAL,
                roll REAL,
                pitch REAL,
                yaw REAL,
                prediction INTEGER,
                feedback INTEGER
            )
        """)
        self.connection.commit()
    
    def save_feedback(self, sample: dict):
        self.cursor.execute("""
            INSERT INTO feedback (x, y, z, roll, pitch, yaw, prediction, feedback)
            VALUES (:x, :y, :z, :roll, :pitch, :yaw, :prediction, :feedback)
        """, sample)
        self.connection.commit()
    
    def load_feedback(self):
        self.cursor.execute("SELECT * FROM feedback")
        rows = self.cursor.fetchall()
        return pd.DataFrame(rows, columns=["id", "x", "y", "z", "roll", "pitch", "yaw", "prediction", "feedback"])
    
    def clear_feedback(self):
        self.cursor.execute("DELETE FROM feedback")
        self.connection.commit()
