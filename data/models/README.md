# Übersicht der Datenmodelle

## Einführung
In diesem Verzeichnis befinden sich die Datenmodelle, die vom integrierten Sensorsystem verwendet werden. Hier finden Sie Beschreibungen, Spezifikationen und Anwendungsfälle der verschiedenen Modelle.

## Verwendung
Nutzen Sie diese Modelle zur Verarbeitung und Analyse der Sensordaten. Die Modelle sind so aufgebaut, dass sie einfach in bestehende Prozesse integriert werden können.

## Modellkonfiguration
Die folgenden Parameter sind in der Konfiguration definiert:
- contamination: 0.05 - Anteil der Anomalien im Datensatz.
- random_state: 42 - Zufallsstartwert für reproduzierbare Ergebnisse.
- n_estimators: 100 - Anzahl der Bäume im Ensemble-Verfahren.
- save_path: "data/models/model.pkl" - Speicherort für das trainierte Modell.
