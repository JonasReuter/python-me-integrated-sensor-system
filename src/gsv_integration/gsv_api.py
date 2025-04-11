"""
GSV API

Dieses Modul stellt eine API zur Steuerung und Datenerfassung von GSV Messverstärkern bereit.
"""

from .gsv_driver import GSVDriver

class GSVAPI:
    def __init__(self, port: int, baud_rate: int, device_id: str):
        self.driver = GSVDriver(port, baud_rate, device_id)

    def get_sensor_data(self):
        """
        Ruft Messdaten vom GSV Gerät ab.
        """
        data = self.driver.read_data()
        return data

    def shutdown(self):
        """
        Schließt die Verbindung zum GSV Gerät.
        """
        self.driver.close_connection()
