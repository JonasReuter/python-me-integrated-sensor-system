import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from ..base_model import BaseAnomalyModel

class IsolationForestModel(BaseAnomalyModel):
    def __init__(self, contamination=0.05, n_estimators=100, random_state=None):
        self.model = IsolationForest(contamination=contamination, n_estimators=n_estimators, random_state=random_state)
    
    def train(self, X):
        self.model.fit(X)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def decision_function(self, X):
        return self.model.decision_function(X)
