import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Entfernt Ausreißer basierend auf einem z-Wert-Schwellenwert.
    """
    # Fix: Division durch 0 absichern - Standardabweichungen von 0 werden auf 1 gesetzt.
    std = df.std().replace(0, 1)
    # Berechnung des z-Scores
    z_scores = (df - df.mean()) / std
    # Filter: Alle Zeilen beibehalten, bei denen in jeder Spalte der |z-Wert| < 3 ist.
    filtered = (np.abs(z_scores) < 3).all(axis=1)
    return df[filtered]

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalisiert die Daten mittels Min-Max-Skalierung.
    """
    # Fix: Verhindert Division durch 0, wenn der Unterschied (max - min) 0 ist.
    diff = df.max() - df.min()
    diff[diff == 0] = 1
    return (df - df.min()) / diff