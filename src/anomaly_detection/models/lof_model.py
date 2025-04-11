from sklearn.neighbors import LocalOutlierFactor
from ..base_model import BaseAnomalyModel

class LOFModel(BaseAnomalyModel):
    def __init__(self, n_neighbors=20, contamination=0.05):
        # Setze novelty=True, um Vorhersagen auf neuen Daten zu ermöglichen
        self.model = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination, novelty=True)
    
    def train(self, X):
        self.model.fit(X)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def decision_function(self, X):
        return self.model.decision_function(X)
