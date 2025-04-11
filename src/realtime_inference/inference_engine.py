import time
import threading
import pandas as pd
from queue import Queue
import logging

class InferenceEngine:
    def __init__(self, model, polling_interval: float = 0.5):
        self.model = model
        self.polling_interval = polling_interval
        self.data_queue = Queue()
        self.is_running = False
        self.thread = None
        self.logger = logging.getLogger(__name__)

    def add_data(self, data: pd.DataFrame):
        self.data_queue.put(data)
        self.logger.debug("Daten zur Queue hinzugefügt.")

    def _process_data(self):
        while self.is_running:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                predictions = self.model.predict(data)
                self.logger.info(f"Inferenz-Ergebnisse: {predictions}")
            else:
                time.sleep(self.polling_interval)

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._process_data)
        self.thread.start()
        self.logger.info("Inference Engine gestartet.")

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
        self.logger.info("Inference Engine gestoppt.")
