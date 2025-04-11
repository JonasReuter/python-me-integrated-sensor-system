"""
GSV API

Dieses Modul stellt eine API zur Steuerung und Datenerfassung von GSV Messverstärkern bereit.
"""
from .gsv_driver import GSVDriver
from src.utils.config_utils import load_config

class GSVAPI:
    def __init__(self, simulation: bool = True):
        config = load_config()
        gsv_conf = config.get("gsv", {})
        self.port = gsv_conf.get("port", 5000)
        self.baud_rate = gsv_conf.get("baud_rate", 9600)
        self.device_id = gsv_conf.get("device_id", "GSV-001")
        self.simulation = simulation
        self.driver = None

    def connect(self):
        """
        Baut die Verbindung zum GSV Gerät auf.
        """
        self.driver = GSVDriver(self.port, self.baud_rate, self.device_id, simulation=self.simulation)
        if not self.simulation and not self.driver:
            raise ConnectionError("Verbindung zum GSV Gerät konnte nicht aufgebaut werden.")
        print("Verbindung zum GSV Gerät hergestellt.")

    def get_sensor_data(self):
        """
        Ruft Messdaten vom GSV Gerät ab.
        """
        if self.driver is None:
            raise RuntimeError("Keine Verbindung: Bitte zuerst connect() aufrufen.")
        try:
            data = self.driver.read_data()
            return data
        except Exception as e:
            print(f"Fehler beim Abrufen der Sensordaten: {e}")
            return None

    def disconnect(self):
        """
        Schließt die Verbindung zum GSV Gerät.
        """
        if self.driver is None:
            print("Keine aktive Verbindung vorhanden.")
            return
        try:
            self.driver.close_connection()
            print("Verbindung zum GSV Gerät wurde geschlossen.")
        except Exception as e:
            print(f"Fehler beim Schließen der Verbindung: {e}")
