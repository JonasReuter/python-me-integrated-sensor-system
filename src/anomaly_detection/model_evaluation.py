from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_model(y_true, y_pred):
    """
    Bewertet die Modellleistung anhand von Precision, Recall und F1-Score.
    """
    metrics = {
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1_score": f1_score(y_true, y_pred, zero_division=0)
    }
    return metrics
