import asyncio
from shared.core.config import settings
from SQL.sql_connection import ConnectionTOSQL
from recive_data_info.consumer_damage import DamageProcessing
from recive_data_info.consumers_intell import IntelProcessing
from recive_data_info.consumer_attack import AttackProcessing
from shared.kafka.consumer import ConsumerMeneage

async def main():
    db_manager = ConnectionTOSQL()
    db_manager.init_db()

    intel_base = ConsumerMeneage(
        settings.BOOTSTRAP_SERVERS,
        [settings.KAFKA_TOPIC_INTEL],
        settings.KAFKA_GROUP_INTEL
    )
    attack_base = ConsumerMeneage(
        settings.BOOTSTRAP_SERVERS,
        [settings.KAFKA_TOPIC_ATTACK],
        settings.KAFKA_GROUP_ATTACK
    )
    damage_base = ConsumerMeneage(
        settings.BOOTSTRAP_SERVERS,
        [settings.KAFKA_TOPIC_DAMAGE],
        settings.KAFKA_GROUP_DAMAGE
    )

    processors = [
        IntelProcessing(intel_base),
        AttackProcessing(attack_base),
        DamageProcessing(damage_base)
    ]

    await asyncio.gather(*(p.start() for p in processors))

if __name__ == "__main__":
    asyncio.run(main())