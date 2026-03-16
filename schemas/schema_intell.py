from pydantic import BaseModel, Field
from typing import Literal
from uuid import UUID, uuid4
from datetime import datetime

class IntelligenceSignalStrem(BaseModel):
    timestamp: datetime = Field(default_factory=lambda:datetime.now())
    signal_id: UUID = Field(default_factory=uuid4)
    entity_id: str
    reported_lat: float
    reported_lon: float 
    signal_type: Literal["VISINT","SIGINT","HUMINT"]
    priority_level: int = Field(ge=1, le=99)