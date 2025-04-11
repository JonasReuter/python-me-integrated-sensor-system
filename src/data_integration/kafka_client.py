from kafka import KafkaConsumer, KafkaProducer
from src.utils.config_utils import load_config

def create_consumer(topic: str, bootstrap_servers: list = None):
    config = load_config()
    kafka_conf = config.get("kafka", {})
    if bootstrap_servers is None:
        bootstrap_servers = kafka_conf.get("bootstrap_servers", ["localhost:9092"])
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
    return consumer

def create_producer(bootstrap_servers: list = None):
    config = load_config()
    kafka_conf = config.get("kafka", {})
    if bootstrap_servers is None:
        bootstrap_servers = kafka_conf.get("bootstrap_servers", ["localhost:9092"])
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    return producer
