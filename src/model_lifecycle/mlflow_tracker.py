import mlflow

def log_experiment(params: dict, metrics: dict):
    """
    Loggt Parameter und Metriken eines Experimentes mit MLflow.
    """
    mlflow.log_params(params)
    mlflow.log_metrics(metrics)
