# API Reference

Diese API Reference beschreibt alle Module und Funktionen des integrierten Systems.

## Module und ihre Funktionen

- **src/config/:**  
  Konfigurationsdateien und Standardparameter (z. B. `default_config.yaml`).

- **src/data_integration/:**  
  Funktionen zur Anbindung von Messaging-Systemen (Kafka) und Persistenz (DB-Connectoren).

- **src/data_preprocessing/:**  
  Vorverarbeitung und Feature Extraction der Sensordaten.

- **src/anomaly_detection/:**  
  Module zur Anomalieerkennung, Trainings-Pipelines, Evaluierung und konkrete Modelle (Isolation Forest, Autoencoder).

- **src/visualization/:**  
  Visualisierungsfunktionen für multidimensionale Daten.

- **src/realtime_inference/:**  
  Echtzeit-Inferenz-Engine zur Verarbeitung von Datenströmen.

- **src/dashboard/:**  
  Interaktive Dashboards und Webapps.

- **src/model_lifecycle/:**  
  Integration von MLflow und Optuna für Experimenttracking und Optimierung.

- **src/api/:**  
  REST-Endpunkte (z. B. via FastAPI).

- **src/online_learning/:**  
  Online Learning-Module für Nutzerfeedback und Retraining.

- **src/gsv_integration/:**  
  Adapter und API-Wrapper für die GSV Messverstärker von me‑systeme.

- **src/utils/:**  
  Hilfsfunktionen (Logging, Konfiguration).

Bitte konsultieren Sie die Inline-Dokumentation in den jeweiligen Modulen für weitere Details.
