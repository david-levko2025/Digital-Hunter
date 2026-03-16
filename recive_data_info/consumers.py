from shared.kafka.consumer import ConsumerMeneage
from shared.core.config import settings

class Manager:
    def __init__(self):
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.topic_intel = settings.KAFKA_TOPIC_INTEL
        self.topic_attack = settings.KAFKA_TOPIC_ATTACK
        self.topic_damage = settings.KAFKA_TOPIC_DAMAGE
        self.group_id = settings.KAFKA_GROUP_ID
        self.consumer : ConsumerMeneage() = None  # type: ignore

    async def setup(self):
        pass
        # self.consumer = ConsumerMeneage(
        #     bootstarp_servers=self.bootstrap_servers,
        #     group_id=self.group_id,
        #     topics=self.topic_attack  /
        # )