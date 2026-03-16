from pydantic import BaseModel,Field
import datetime


class DamageAssessment(BaseModel):
    timestamp: datetime.datetime = Field()
    attack_id: str = Field()
    entity_id: str = Field()
    result :str = Field()