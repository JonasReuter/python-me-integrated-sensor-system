import logging

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s: %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
