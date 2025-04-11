# User Guide

Diese Anleitung führt Sie durch Installation, Konfiguration und Nutzung des integrierten Systems.

## Installation

Befolgen Sie die Schritte in der Haupt-README.md zur Installation des Systems.

## Nutzung

- **Datenintegration:**  
  Nutzen Sie die Module unter `src/data_integration/` zum Erfassen von Echtzeitdaten, z. B. über Kafka, und zur Persistierung in Datenbanken.

- **Anomalieerkennung:**  
  Trainieren und evaluieren Sie Modelle unter `src/anomaly_detection/`. Verwenden Sie die Feedback-Module in `src/online_learning/`, um das System im Betrieb adaptiv zu verbessern.

- **Visualisierung:**  
  Verwenden Sie die Module in `src/visualization/` zur Darstellung der Sensordaten (Pairplots, 3D-Scatterplots, etc.).

- **GSV Integration:**  
  Über `src/gsv_integration/` können GSV Messverstärker von me‑systeme direkt angebunden werden, sodass die präzise Messdatenerfassung out of the box möglich ist.

- **API & Dashboards:**  
  Greifen Sie über die REST-Endpunkte in `src/api/` oder über interaktive Dashboards in `src/dashboard/` auf das System zu.

Weitere Details finden Sie in der API Reference.
