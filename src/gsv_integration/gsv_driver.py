"""
GSV Driver

Dieses Modul implementiert einen Adapter/Wrapping-Mechanismus für die GSV Messverstärker-Bibliotheken.
Stellen Sie sicher, dass die erforderlichen GSV Python 3 Bibliotheken installiert sind.
"""

class GSVDriver:
    def __init__(self, port: int, baud_rate: int, device_id: str, simulation: bool = True):
        self.port = port
        self.baud_rate = baud_rate
        self.device_id = device_id
        self.simulation = simulation
        # Initialisierung der GSV-Bibliothek (hier als Platzhalter)
        self.connection = self._initialize_connection()

    def _initialize_connection(self):
        if self.simulation:
            print(f"[SIMULATION] Verbinde zu GSV Gerät {self.device_id} an Port {self.port} mit Baudrate {self.baud_rate}")
            return True
        else:
            try:
                from gsv8pypi_python3 import GSVConnection
            except ImportError:
                raise ImportError("gsv8pypi_python3 library is not installed.")
            # Erstelle und initialisiere die Live-Verbindung.
            connection = GSVConnection(port=self.port, baud_rate=self.baud_rate, device_id=self.device_id)
            connection.connect()  # Verbindungsaufbau
            return connection
    
    def read_data(self):
        if self.simulation:
            # Simuliere realistischere Daten
            import random
            data = {
                "x": round(random.uniform(0, 1), 2),
                "y": round(random.uniform(0, 1), 2),
                "z": round(random.uniform(0, 1), 2),
                "roll": round(random.uniform(-0.1, 0.1), 2),
                "pitch": round(random.uniform(-0.1, 0.1), 2),
                "yaw": round(random.uniform(-0.1, 0.1), 2),
            }
            return data
        else:
            # Live-Daten über die gsv8pypi_python3-Bibliothek abrufen.
            return self.connection.get_sensor_data()  # Annahme: Methode get_sensor_data() existiert

    def close_connection(self):
        if self.simulation:
            print("[SIMULATION] Verbindung zu GSV Gerät geschlossen.")
        else:
            self.connection.disconnect()  # Annahme: disconnect() beendet die Verbindung
            print("Verbindung zu GSV Gerät geschlossen.")
