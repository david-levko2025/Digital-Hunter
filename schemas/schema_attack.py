from pydantic import BaseModel,Field
from datetime import datetime
from uuid import UUID, uuid4

class AirForceAttack(BaseModel):
    timestamp: datetime = Field(default_factory=lambda:datetime.now())
    attack_id: UUID = Field(default_factory= uuid4)
    entity_id: str = Field()
    weapon_type : str =  Field()