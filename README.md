# Integriertes Ökosystem für Anomalieerkennung, Visualisierung und Datenintegration
## mit Anbindung an die GSV Messverstärker von me‑systeme

Dieses Projekt stellt ein umfassendes System bereit, das Hardware und Software zu einer Komplettlösung vereint. Es umfasst:

- **Anomalieerkennung:**  
  Flexible Module zur Vorverarbeitung, Modellierung und Evaluierung von Sensordaten (1D bis 6D) mittels Algorithmen wie Isolation Forest und Autoencoder.

- **Multidimensionale Visualisierung:**  
  Verschiedene Visualisierungsansätze – darunter Paar‑Plots, 3D‑Scatterplots, Parallel Coordinates und Dimensionsreduktion (PCA, t‑SNE, UMAP) – um Messdaten anschaulich darzustellen.

- **Datenintegration:**  
  Komponenten für den Echtzeit‑Datenempfang (über Messaging-Systeme wie Kafka) und die Anbindung an Datenbanken (SQL, NoSQL, Elasticsearch).

- **Online Learning & Feedback:**  
  Ein adaptives Modul, das Nutzerfeedback bei erkannten Anomalien erfasst und in regelmäßigen Retraining‑Zyklen das Modell kontinuierlich verbessert.

- **API & Dashboards:**  
  Bereitstellung von REST‑Endpoints (mit FastAPI/Flask) und interaktiven Dashboards (etwa mit Dash oder Streamlit) zur Echtzeit‑Überwachung und Datenanalyse.

- **Modellmanagement & Experimenttracking:**  
  Integration von Tools wie MLflow und Optuna für Training, Hyperparameter‑Optimierung und Versionierung.

- **Entwicklungsunterstützung:**  
  Zusätzliche Dev‑Tools (wie Flake8, Black, mypy, Sphinx) und umfassende Dokumentation.

- **Integration der GSV Messverstärker von me‑systeme:**  
  Das System schließt speziell auch die Anbindung an die GSV Messverstärker ein – Hardwarekomponenten, wie sie in den offiziellen GitHub-Repositorien von me‑systeme dokumentiert sind. Diese Messverstärker gewährleisten eine präzise Signalkonditionierung und bieten flexible Schnittstellen für den direkten Anschluss an Sensornetzwerke in industriellen Anwendungen. Über bereitgestellte Treiber und APIs lässt sich die Hardware nahtlos in das Ökosystem einbinden. Somit können Sie als Sensorhersteller nicht nur hochwertige Sensorhardware bereitstellen, sondern auch eine vollständige Lösung zur Datenerfassung, -analyse und -visualisierung in einem integrierten System anbieten.

## Projektstruktur

```
integrated_system/
├── README.md                      # Haupt-README (dieses Dokument)
├── setup.py                       # Installations-Skript
├── requirements.txt               # Python-Abhängigkeiten
├── dev-requirements.txt           # Zusätzliche Dev-Tools (z. B. Flake8, Black, mypy, Sphinx)
├── .gitignore                     # Zu ignorierende Dateien
├── Dockerfile                     # Docker-Datei zur Containerisierung
├── docker-compose.yml             # (Optional) Docker Compose Konfiguration
│
├── docs/                          # Dokumentation
│   ├── index.md                 
│   ├── user_guide.md              
│   └── api_reference.md           
│
├── data/                          # Datenverzeichnisse
│   ├── raw/                      # Ursprüngliche Sensordaten
│   │   └── README.md             
│   ├── processed/                # Vorverarbeitete Daten
│   │   └── README.md             
│   └── external/                 # Externe Datensätze & Benchmarks
│       └── README.md             
│
├── src/                           # Hauptquellcode (modulare Sub-Pakete)
│   ├── __init__.py
│   │
│   ├── config/                    # Konfigurationen und Standardparameter
│   │   ├── __init__.py
│   │   └── default_config.yaml    
│   │
│   ├── data_integration/          # Messaging und Datenbankanbindung
│   │   ├── __init__.py            
│   │   ├── kafka_client.py         # Beispiel-Implementierung für Kafka
│   │   └── db_connector/           # Abstraktion der Persistenzschicht
│   │       ├── __init__.py
│   │       ├── sql_connector.py    # SQL-Connector (z. B. SQLAlchemy)
│   │       ├── nosql_connector.py  # NoSQL-Connector (z. B. MongoDB/PyMongo)
│   │       └── elasticsearch_connector.py  # Elasticsearch-Connector
│   │
│   ├── data_preprocessing/           # Vorverarbeitung, Bereinigung und Feature Extraction
│   │   ├── __init__.py
│   │   └── transformer.py
│   │
│   ├── anomaly_detection/         # Anomalie-Erkennungs-Module
│   │   ├── __init__.py            
│   │   ├── base_model.py          # Abstrakte Basisklasse für Modelle
│   │   ├── model_training.py      # Trainings-Pipeline und Hyperparameter-Tuning
│   │   ├── model_evaluation.py    # Evaluationsmetriken
│   │   └── models/                # Konkrete Modellimplementierungen
│   │       ├── isolation_forest_model.py
│   │       └── autoencoder_model.py
│   │
│   ├── visualization/             # Visualisierungsbibliothek
│   │   ├── __init__.py
│   │   ├── pairplot.py            # Paar-/Scatterplot-Matrix
│   │   ├── scatter3d.py           # 3D-Scatterplot-Funktionen (z. B. mit Plotly)
│   │   ├── parallel_coords.py     # Parallel Coordinates Plots
│   │   └── reduction.py           # Dimensionsreduktion (PCA, t-SNE, UMAP) inkl. Plotfunktionen
│   │
│   ├── realtime_inference/        # Echtzeit-/Streaming-Inferenz
│   │   ├── __init__.py
│   │   └── inference_engine.py    # Implementierung der Inference Engine
│   │
│   ├── dashboard/                 # Interaktive Dashboards und Webapps
│   │   ├── __init__.py
│   │   └── interactive.py         # Beispielmodule (z. B. mit Dash oder Streamlit)
│   │
│   ├── model_lifecycle/           # Experimenttracking, Versionierung und Hyperparameter-Optimierung
│   │   ├── __init__.py
│   │   ├── mlflow_tracker.py      # Integration mit MLflow
│   │   └── optimizer.py           # Hyperparameter-Optimierung (z. B. mit Optuna)
│   │
│   ├── api/                       # API-Schicht (REST-Endpunkte)
│   │   ├── __init__.py
│   │   └── main_api.py            # Endpunkte (z. B. FastAPI oder Flask)
│   │
│   ├── online_learning/           # Online Learning & Feedback-Module
│   │   ├── __init__.py
│   │   └── online_learning.py     # Funktionen zum Speichern von Feedback und Retraining
│   │
│   └── utils/                     # Hilfsfunktionen (Logging, Konfiguration, etc.)
│       ├── __init__.py
│       ├── logging_utils.py
│       └── config_utils.py
│
├── tests/                         # Unit- und Integrationstests
│   ├── __init__.py
│   ├── test_data_preprocessing.py
│   ├── test_anomaly_detection.py
│   ├── test_visualization.py
│   └── test_api.py
│
└── examples/                      # Beispielskripte und Jupyter-Notebooks
    ├── example_notebook.ipynb
    └── plug_n_play_with_feedback.py   # Plug n Play Script inkl. Feedback-Engine & DB-Anbindung
```

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/JonasReuter/python-me-integrated-sensor-system.git
   cd python-me-integrated-sensor-system
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional:** Zusätzliche Dev-Tools aus `dev-requirements.txt` installieren:
   ```bash
   pip install -r dev-requirements.txt
   ```

4. **Bibliothek installieren:**
   ```bash
   python setup.py install
   ```

5. **(Optional) Mit Docker starten:**
   ```bash
   docker-compose up --build
   ```

## Einsatzszenarien

- **Industrielle Fertigung & Maschinenbau:**  
  Echtzeitüberwachung von Anlagen, Predictive Maintenance und Optimierung von Fertigungsprozessen.

- **Medizintechnik:**  
  Überwachung und Diagnose von medizinischen Geräten sowie Rehabilitationsprozessen.

- **Edge-Computing:**  
  Optimierte Modelle laufen auch auf eingebetteten Systemen.

- **Interaktive Dashboards:**  
  Visuelle Analyse und Echtzeitüberwachung per Webinterface.

- **Integration mit GSV Messverstärkern von me‑systeme:**  
  Nutzen Sie die Schnittstellen (wie in den offiziellen GitHub-Repositorien dokumentiert), um GSV Messverstärker in unser Ökosystem zu integrieren. Dadurch erhalten Sie präzise, verstärkte Sensordaten, die nahtlos in unsere Plattform eingebunden werden können – ideal zur Erfassung und Echtzeitverarbeitung in industriellen Anwendungen.

## Online Learning & Nutzerfeedback

Das System sammelt bei erkannten Anomalien Nutzerfeedback („y“ für bestätigte Anomalie, „n“ für False Positive). Dieses Feedback wird über die Datenbank-Connectoren persistiert und in regelmäßigen Retraining-Zyklen genutzt, um die Modelle kontinuierlich zu verbessern.

## Weiterführende Dokumentation

Detaillierte Informationen zur Nutzung der einzelnen Module finden Sie in:
- [User Guide](docs/user_guide.md)
- [API Reference](docs/api_reference.md)

## Lizenz & Mitwirkende

Dieses Projekt steht unter der [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  
Bitte beachten Sie die Lizenzbedingungen für die Nutzung, Modifikation und Weiterverbreitung des Codes.

### Mitwirkende
- Jonas Reuter
- Weitere Mitwirkende können über Pull Requests hinzugefügt werden.

---

## Hinweis: Work in Progress

**Dieses Projekt befindet sich derzeit in der Entwicklung und ist als Konzept zu betrachten.**  
Der Code wird schrittweise erweitert, getestet und funktional hergestellt. Bis zur Fertigstellung können Teile des Systems unvollständig oder nicht funktionsfähig sein. Dieser Hinweis wird entfernt, sobald das Projekt stabil und einsatzbereit ist.

---

Dieses integrierte Ökosystem verbindet Hardware (z. B. GSV Messverstärker von me‑systeme) und Software (Datenanalyse, Visualisierung, Online Learning, API und Dashboard) zu einer Komplettlösung für industrielle Anwendungen. Es ermöglicht nicht nur die präzise Messdatenerfassung, sondern liefert auch adaptive, datengesteuerte Prozesse, die neue Geschäftsmodelle wie Predictive Maintenance as a Service, digitale Zwillinge und datenbasierte Serviceangebote unterstützen.

Viel Erfolg bei der Implementierung und Weiterentwicklung des Systems!
