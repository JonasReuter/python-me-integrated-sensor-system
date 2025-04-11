# Übersicht der Anomaly Detection Modelle

## Modelle und ihre Eigenschaften & Einsatzbereiche

- **IsolationForestModel**  
  - **Vorteile:**  
    - Schnelle und robuste Erkennung von Ausreißern
    - Hohe Skalierbarkeit bei großen Datenmengen  
  - **Praxisnaher Einsatz:**  
    - Ideal für Produktionsumgebungen, in denen Sensordaten von Maschinen (z. B. 1-6D Kraftsensoren) in Echtzeit überwacht werden.
    - Einsatz in Fertigungsstraßen zur frühzeitigen Fehlererkennung und Predictive Maintenance.
  - **Einsatzbereich:**  
    - Industrie 4.0 sowie Prozesse, in denen schnelle Entscheidungen auf Basis statistischer Ausreißer notwendig sind.

- **AutoencoderModel**  
  - **Vorteile:**  
    - Lernt komplexe nichtlineare Zusammenhänge
    - Kann verdeckte Strukturen in hochdimensionalen Daten entdecken  
  - **Praxisnaher Einsatz:**  
    - Optimal bei komplexen Anlagen, z. B. in der chemischen Produktion oder bei der Überwachung von IT-Infrastrukturen, in denen viele verschiedene Sensoren eingesetzt werden.
    - Verwendung in der Qualitätskontrolle, um subtile Abweichungen im Produktionsprozess zu identifizieren.
  - **Einsatzbereich:**  
    - Anwendungen, bei denen große Mengen an Detaildaten analysiert werden müssen und frühe Warnsignale komplexer Prozesse entscheidend sind.

- **OneClassSVMModel**  
  - **Vorteile:**  
    - Klassische One-Class Klassifikation, die leicht zu interpretieren ist.
    - Gut geeignet, wenn klare Trennlinien zwischen normal und anormal vorhanden sind  
  - **Praxisnaher Einsatz:**  
    - Einsatz in Szenarien, in denen Sensordaten klare Betriebsschwellwerte aufweisen, beispielsweise bei Überwachung von Energiedaten in Gebäuden oder bei präzisen Kraftmessungen.
    - Unterstützt Entscheidungsprozesse in regelbasierten Systemen, wo anormale Werte schnell isoliert werden müssen.
  - **Einsatzbereich:**  
    - Anwendungen mit weniger variablen, aber kritischen Sensordaten, z. B. Sicherheitsüberwachung oder Prozesskontrolle in industriellen Anlagen.

- **LOFModel (Local Outlier Factor)**  
  - **Vorteile:**  
    - Erkennt lokale Dichteabweichungen und eignet sich für heterogene Datenverteilungen.
    - Robust gegenüber variierenden Betriebsbedingungen  
  - **Praxisnaher Einsatz:**  
    - Einsatz in vernetzten Systemen, etwa in einem Smart Factory-Umfeld, wo Sensoren in unterschiedlichen Netzwerksegmenten betrieben werden.
    - Anwendbar bei komplexen Sensornetzwerken, wo lokale Unregelmäßigkeiten (z. B. sporadische Ausfallzeiten oder kurzfristige Lastspitzen) erkannt werden sollen.
  - **Einsatzbereich:**  
    - Besonders geeignet für industrielle IoT-Anwendungen und Szenarien, in denen Umgebungsbedingungen stark variieren und eine dynamische Erkennung erforderlich ist.

## Empfehlungen für den praktischen Einsatz

- **Für einzelne oder wenige Kraftsensoren (1-6D):**  
  IsolationForestModel oder OneClassSVMModel bieten eine schnelle und präzise Erkennung, die sich ideal für Echtzeitüberwachung und Predictive Maintenance eignet.

- **Für komplexe Anwendungen mit vielen heterogenen Sensoren:**  
  AutoencoderModel und LOFModel sind zu bevorzugen, da sie sowohl nichtlineare Zusammenhänge als auch lokale Dichteabweichungen erfassen können. Diese Modelle eignen sich insbesondere, wenn ein tieferes Verständnis der Sensordaten erforderlich ist, beispielsweise in vernetzten Produktionsumgebungen (Smart Factory) oder in der Überwachung umfangreicher IT-Infrastrukturen.

- **Allgemeine Hinweise:**  
  Die Wahl des Modells hängt stark von den spezifischen Betriebsbedingungen, der Datenmenge und der erforderlichen Reaktionsgeschwindigkeit ab. Es empfiehlt sich, in Pilotprojekten mehrere Modelle zu testen und deren Performance auf die konkreten Anwendungsfälle abzustimmen.
