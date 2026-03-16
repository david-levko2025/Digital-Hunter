from pydantic import BaseModel,Field
from datetime import datetime


class DamageAssessment(BaseModel):
    timestamp : datetime = Field(default_factory=lambda:datetime.now())
    attack_id : str
    entity_id : str
    result : str

    