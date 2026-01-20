from src.config.mongo_config import get_database
from src.model.sensor_model import Sensor
from bson.objectid import ObjectId
import uuid

db = get_database()
collection = db["sensors"]

class SensorService:

    def create_sensor(self, sensor: Sensor):
        # Generamos un ID si no viene uno
        sensor_dict = sensor.dict(by_alias=True, exclude={"elementId"})
        sensor_dict["_id"] = str(uuid.uuid4()) # O usa ObjectId de mongo
        sensor_dict["last_update"] = datetime.now()
        
        result = collection.insert_one(sensor_dict)
        return str(result.inserted_id)

    def get_all_sensors(self):
        sensors = []
        for doc in collection.find():
            # Convertir _id a string para el modelo
            doc["elementId"] = str(doc["_id"])
            sensors.append(Sensor(**doc))
        return sensors

    def get_sensor_by_id(self, sensor_id: str):
        doc = collection.find_one({"_id": sensor_id})
        if doc:
            doc["elementId"] = str(doc["_id"])
            return Sensor(**doc)
        return None

    def update_status(self, sensor_id: str, new_status: str):
        collection.update_one(
            {"_id": sensor_id},
            {"$set": {"status": new_status, "last_update": datetime.now()}}
        )
        return {"msg": "Status updated"}

    def delete_sensor(self, sensor_id: str):
        result = collection.delete_one({"_id": sensor_id})
        return result.deleted_count > 0
