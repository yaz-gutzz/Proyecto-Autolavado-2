from fastapi import FastAPI
from typing import List
from uuid import uuid4
from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Yazmin",
        apellidos="Gutierrez",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Obed",
        apellidos="Guzman",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/users")
async def get_users():
    return db
