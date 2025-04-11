import yaml
import os

def load_config(config_path: str = "src/config/default_config.yaml") -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Konfigurationsdatei nicht gefunden: {config_path}")
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config
