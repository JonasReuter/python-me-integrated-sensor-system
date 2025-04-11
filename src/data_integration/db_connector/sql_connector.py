from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

class SQLConnector:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def execute_query(self, query: str):
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result.fetchall()

    def save_feedback(self, feedback: dict, table_name: str = "feedback"):
        df = pd.DataFrame([feedback])
        df.to_sql(table_name, con=self.engine, if_exists='append', index=False)
