from shared.log.logger import log_event
from schemas.schema_intell import IntelligenceSignalStrem
from SQL.sql_connection import ConnectionTOSQL

class IntelProcessing:
    def __init__(self,consumer_base):
        self.consumer = consumer_base
        self.db = ConnectionTOSQL()
        self.service_name = "intel-service"
    
    async def process(self, data):
        try:
            signal = IntelligenceSignalStrem(**data)
            target = self.db.get_target(signal.entity_id)
            if target and target['result'] == "destroyed":
                log_event("DEBUG",f"target {signal.entity_id} destroyed",self.service_name)
                return
                  
            priority_level = 99 if not target else signal.priority_level

            self.db.upsert_target(
                entity_id = signal.entity_id,
                lat = signal.reported_lat,
                lon = signal.reported_lon,
                priority = priority_level,
                signal_type = signal.signal_type
            )
            log_event("INFO",f"target {signal.entity_id} updated",self.service_name)

        except Exception as e:
            log_event("ERROR",f"error in the intel processing: {e}",self.service_name)

    async def start(self):
        await self.consumer.consumer_loop(self.process)




