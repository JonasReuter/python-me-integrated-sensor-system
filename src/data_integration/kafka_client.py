from kafka import KafkaConsumer, KafkaProducer

def create_consumer(topic: str, bootstrap_servers: list):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
    return consumer

def create_producer(bootstrap_servers: list):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    return producer
