from shared.kafka.producer import ProducerManager
from shared.core.config import settings

class Manger:
    def __init__(self):
        self.producer : ProducerManager() | None = None  # type: ignore
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.group_id = settings.KAFKA_GROUP_ID
        self.topic =settings.KAFKA_TOPIC_DAMAGE

    async def setup(self):
        self.producer = ProducerManager(
            bootstarp_servers= self.bootstrap_servers,
            topic=self.topic
        )