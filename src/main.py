import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controller import sensor_controller # Importar el nuevo controlador

app = FastAPI(title="Sensor Service", version="1.0.0")

# Configurar CORS (Importante para que el Frontend hable con él)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(sensor_controller.router)

if __name__ == "__main__":
    # Correr en el puerto 10051 (o el que tengas asignado en tu arquitectura)
    uvicorn.run("src.main:app", host="0.0.0.0", port=10051, reload=True)
