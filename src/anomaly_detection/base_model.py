from abc import ABC, abstractmethod

class BaseAnomalyModel(ABC):
    @abstractmethod
    def train(self, X):
        """
        Trainiert das Modell mit den Daten X.
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Gibt Vorhersagen bzw. Anomalie-Scores für die Daten X zurück.
        """
        pass
