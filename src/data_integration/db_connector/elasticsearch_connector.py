from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd

class ElasticsearchConnector:
    def __init__(self, hosts: list):
        self.es = Elasticsearch(hosts)

    def index_feedback(self, index: str, feedback: dict):
        res = self.es.index(index=index, body=feedback)
        return res

    def bulk_index_feedback(self, index: str, df: pd.DataFrame):
        actions = [
            {
                "_index": index,
                "_source": row.to_dict()
            }
            for _, row in df.iterrows()
        ]
        success, _ = bulk(self.es, actions)
        return success
