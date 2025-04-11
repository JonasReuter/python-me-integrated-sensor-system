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
                from gsv8pypi_python3.gsv8 import gsv8  # lokaler Import der gsv8-Klasse
            except ImportError:
                raise ImportError("Lokale gsv8 Treiber nicht gefunden.")
            try:
                # Erzeuge ein gsv8-Objekt (Parameter: port, baudrate)
                connection = gsv8(port=self.port, baudrate=self.baud_rate)
                # Falls weitere Initialisierung notwendig ist, kann hier z.B. ein Transmission-Start erfolgen.
                return connection
            except Exception as e:
                raise ConnectionError(f"Fehler beim Herstellen der Verbindung: {e}")
    
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
            # Verwende die ReadValue()-Methode der gsv8 Klasse, um den Messwert zu erhalten
            return self.connection.ReadValue()

    def close_connection(self):
        if self.simulation:
            print("[SIMULATION] Verbindung zu GSV Gerät geschlossen.")
        else:
            self.connection.disconnect()
            print("Verbindung zu GSV Gerät geschlossen.")
