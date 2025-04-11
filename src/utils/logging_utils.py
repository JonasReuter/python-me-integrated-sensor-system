import logging
from src.utils.config_utils import load_config

def setup_logger(name, level=logging.INFO):
    config = load_config()  # Konfiguration laden
    log_config = config.get("logging", {})
    log_level = getattr(logging, log_config.get("level", "INFO"), logging.INFO)
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Standard Stream Handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        # Falls Log-Datei angegeben
        log_file = log_config.get("file")
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    logger.setLevel(log_level)
    return logger
