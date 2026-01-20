from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Sensor(BaseModel):
    elementId: Optional[str] = Field(None, alias='_id')
    name: str                 # Ej: "Sensor-Piso1-A01"
    location: str             # Ej: "Zona Norte, Espacio 10"
    type: str                 # Ej: "ULTRASONIC", "CAMERA", "INDUCTION"
    status: str               # Ej: "FREE", "OCCUPIED", "MAINTENANCE"
    last_update: datetime = datetime.now()
    ip_address: Optional[str] = None
    
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
