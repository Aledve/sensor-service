FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Importante: Copiamos la carpeta 'src' completa dentro de '/code/src' 
# para mantener la estructura de paquetes y que los imports "from src.controller..." funcionen.
COPY src /code/src

# Configuramos el PYTHONPATH para incluir el directorio de trabajo
ENV PYTHONPATH=/code

# Ejecutamos apuntando a la ruta del archivo dentro del paquete
CMD ["python", "src/main.py"]
