"""
Abstraktionsschicht für die Persistenz.

Dieses Modul importiert die spezifischen DB-Connectoren (SQL, NoSQL, Elasticsearch).
"""
from .sql_connector import SQLConnector
from .nosql_connector import NoSQLConnector
from .elasticsearch_connector import ElasticsearchConnector
