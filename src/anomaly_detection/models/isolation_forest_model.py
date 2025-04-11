import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from ..base_model import BaseAnomalyModel

class IsolationForestModel(BaseAnomalyModel):
    def __init__(self, contamination: float = 0.05, n_estimators: int = 100, random_state: int = 42):
        self.model = IsolationForest(contamination=contamination, n_estimators=n_estimators, random_state=random_state)

    def train(self, X: pd.DataFrame):
        self.model.fit(X)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X)
