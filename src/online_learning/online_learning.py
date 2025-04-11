import pandas as pd
from src.anomaly_detection.models.autoencoder_model import AutoencoderModel
from src.anomaly_detection.models.isolation_forest_model import IsolationForestModel
from src.utils.logging_utils import setup_logger

logger = setup_logger("OnlineLearning", level=20)
FEEDBACK_CSV = "feedback_data.csv"

def save_feedback(sample: dict):
    """
    Speichert einen Feedback-Datensatz in einer CSV-Datei.
    """
    df_sample = pd.DataFrame([sample])
    try:
        existing = pd.read_csv(FEEDBACK_CSV)
        df_sample = pd.concat([existing, df_sample], ignore_index=True)
    except FileNotFoundError:
        logger.info("Feedback-Datei wird neu erstellt.")
    df_sample.to_csv(FEEDBACK_CSV, index=False)
    logger.info("Feedback gespeichert.")

def load_feedback():
    try:
        return pd.read_csv(FEEDBACK_CSV)
    except FileNotFoundError:
        logger.info("Keine Feedbackdaten gefunden.")
        return pd.DataFrame()

def retrain_model(model, new_data: pd.DataFrame, epochs: int = 5):
    """
    Retrainiert das Modell anhand der neuen Feedbackdaten.
    """
    if isinstance(model, AutoencoderModel):
        logger.info("Retraining: Fein-Tuning des Autoencoders...")
        model.train(new_data)
        logger.info("Retraining abgeschlossen.")
    elif isinstance(model, IsolationForestModel):
        logger.info("Retraining: Neu-Training des Isolation Forest Modells...")
        model.train(new_data)
        logger.info("Neu-Training abgeschlossen.")
    else:
        logger.error("Unbekannter Modelltyp für Retraining.")
    return model

def online_learning_cycle(model, min_samples: int = 10, epochs: int = 5):
    """
    Prüft, ob genügend Feedbackdaten vorliegen, und führt Retraining aus.
    """
    feedback_df = load_feedback()
    if feedback_df.shape[0] >= min_samples:
        training_data = feedback_df.drop(columns=["prediction", "feedback"], errors="ignore")
        logger.info(f"Retraining mit {training_data.shape[0]} Feedback-Datensätzen.")
        model = retrain_model(model, training_data, epochs=epochs)
        feedback_df.drop(feedback_df.index, inplace=True)
        feedback_df.to_csv(FEEDBACK_CSV, index=False)
    else:
        logger.info("Nicht genügend Feedbackdaten für Retraining vorhanden.")
    return model
