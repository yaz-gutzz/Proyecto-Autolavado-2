# model.py
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Genero(str, Enum):
    masculino = "Hombre"
    femenino = "Mujer"
    otro = "Otro"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    primerNombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
