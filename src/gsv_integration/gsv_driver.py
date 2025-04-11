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
        # TODO: Erweiterte Initialisierungslogik für Live-Betrieb implementieren.
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
            connection = GSVConnection(port=self.port, baud_rate=self.baud_rate, device_id=self.device_id)
            connection.connect()  # TODO: Fehlerbehandlung erweitern.
            return connection
    
    def read_data(self):
        if self.simulation:
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
            # TODO: Live-Datenabruf weiter testen und robust machen.
            return self.connection.get_sensor_data()

    def close_connection(self):
        if self.simulation:
            print("[SIMULATION] Verbindung zu GSV Gerät geschlossen.")
        else:
            self.connection.disconnect()
            print("Verbindung zu GSV Gerät geschlossen.")
