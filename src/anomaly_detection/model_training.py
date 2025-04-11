from .base_model import BaseAnomalyModel

def train_model(model: BaseAnomalyModel, X_train, epochs: int = 10):
    """
    Führt ein Training des Modells für die angegebene Anzahl an Epochen durch.
    """
    for epoch in range(epochs):
        model.train(X_train)
        print(f"Epoch {epoch + 1}/{epochs} abgeschlossen.")
    return model
