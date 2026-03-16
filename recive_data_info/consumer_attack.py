from shared.log.logger import log_event
from schemas.schema_attack import AirForceAttack
from SQL.sql_connection import ConnectionTOSQL

class AttackProcessing:
    def __init__(self,consumer_base):
        self.consumer = consumer_base
        self.db = ConnectionTOSQL()
        self.service_name = "attack-service"
    
    async def process(self, data):
        try:
            attack = AirForceAttack(**data)
            target = self.db.get_target(attack.entity_id)
            if target['result'] == "destroyed":   # type: ignore
                log_event("DEBUG",f"target rejected :{attack.entity_id} already destroyed",self.service_name)
                return

            self.db.insert_attack(
                str(attack.attack_id),
                attack.entity_id,
                weapon_type = attack.weapon_type
            )
            log_event("INFO",f"target {attack.entity_id} updated",self.service_name)

        except Exception as e:
            log_event("ERROR",f"error in the attack processing: {e}",self.service_name)

    async def start(self):
        await self.consumer.consumer_loop(self.process)




