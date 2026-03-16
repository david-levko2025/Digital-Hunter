from shared.log.logger import log_event
from schemas.schema_damage import DamageAssessment
from SQL.sql_connection import ConnectionTOSQL

class DamageProcessing:
    def __init__(self,consumer_base):
        self.consumer = consumer_base
        self.db = ConnectionTOSQL()
        self.service_name = "damage-service"
    
    async def process(self, data):
        try:
            damage = DamageAssessment(**data)
            success = self.db.insert_damage_reports(
                str(damage.attack_id),
                damage.entity_id,
                damage.result
                )
            if success:
                log_event("INFO",f"target {damage.entity_id} updated",self.service_name)
            else:
                log_event("ERROR",f"attack {damage.attack_id} not found",self.service_name)

        except Exception as e:
            log_event("ERROR",f"error in the damage processing: {e}",self.service_name)

    async def start(self):
        await self.consumer.consumer_loop(self.process)




