from fastapi import APIRouter, HTTPException
from src.model.sensor_model import Sensor
from src.service.sensor_service import SensorService

router = APIRouter(prefix="/sensorService", tags=["Sensors"])
service = SensorService()

@router.get("/")
def get_all():
    return service.get_all_sensors()

@router.get("/{elementId}")
def get_by_id(elementId: str):
    sensor = service.get_sensor_by_id(elementId)
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor

@router.post("/")
def create(sensor: Sensor):
    sensor_id = service.create_sensor(sensor)
    return {"elementId": sensor_id, "message": "Sensor created successfully"}

@router.put("/{elementId}/status")
def update_status(elementId: str, status: str):
    # Endpoint crítico para recibir señal de IoT
    service.update_status(elementId, status)
    return {"message": "Sensor status updated"}

@router.delete("/{elementId}")
def delete(elementId: str):
    success = service.delete_sensor(elementId)
    if not success:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return {"message": "Sensor deleted"}
