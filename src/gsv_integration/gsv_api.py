"""
GSV API

Dieses Modul stellt eine API zur Steuerung und Datenerfassung von GSV Messverstärkern bereit.
"""
from .gsv_driver import GSVDriver

class GSVAPI:
    def __init__(self, port: int, baud_rate: int, device_id: str, simulation: bool = True):
        # Verbindung wird nicht automatisch aufgebaut, sondern explizit via connect() initiiert.
        self.port = port
        self.baud_rate = baud_rate
        self.device_id = device_id
        self.simulation = simulation
        self.driver = None

    def connect(self):
        """
        Baut die Verbindung zum GSV Gerät auf.
        """
        self.driver = GSVDriver(self.port, self.baud_rate, self.device_id, simulation=self.simulation)
        # Optional: Überprüfe die Verbindung nach dem Initialisieren
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
            # Fehler beim Schließen der Verbindung protokollieren
            print(f"Fehler beim Schließen der Verbindung: {e}")
