from pymongo import MongoClient
import pandas as pd

class NoSQLConnector:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
    
    def insert_feedback(self, collection_name: str, feedback: dict):
        collection = self.db[collection_name]
        result = collection.insert_one(feedback)
        return result.inserted_id

    def insert_feedback_dataframe(self, collection_name: str, df: pd.DataFrame):
        collection = self.db[collection_name]
        data = df.to_dict(orient='records')
        result = collection.insert_many(data)
        return result.inserted_ids
