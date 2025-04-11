import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Entfernt Ausreißer basierend auf einem z-Wert-Schwellenwert.
    """
    z_scores = np.abs((df - df.mean()) / df.std())
    filtered = (z_scores < 3).all(axis=1)
    return df[filtered]

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalisiert die Daten mittels Min-Max-Skalierung.
    """
    return (df - df.min()) / (df.max() - df.min())
