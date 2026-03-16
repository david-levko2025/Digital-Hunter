import asyncio
import json 
from datetime import datetime
from confluent_kafka import Producer

from shared.core.config import settings
from shared.kafka.consumer import ConsumerMeneage
import simulator
from schemas.schema_intell import IntelligenceSignalStrem

class IntelProcessing:
    def __init__(self,servers,group_id):
        self.consumer = ConsumerMeneage(servers,["intel"],group_id)
        self.topic_dlq = settings.KAFKA_TOPIC_DLQ
    async def process_signals(self,data):
        pass