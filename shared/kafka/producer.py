from confluent_kafka import Producer
import json

class ProducerManager:
    def __init__(self, bootstarp_servers:str, topic:str):
        self.conf = {
            "bootstarp_servers": bootstarp_servers,
        }
        self.producer = Producer(self.conf)
        self.topic = topic

    async def sens_message(self,message: dict):
        """send message to kafka"""
        self.producer.produce(
            topic=self.topic,
            value= json.dumps(message).encode('utf-8')
        )
        self.producer.poll(0)
        
    def close(self):
        """close the connection to kafka"""
        self.producer.flush(10)