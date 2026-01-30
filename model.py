"""
Modelos de datos para la API de usuarios.

Define enums y esquemas Pydantic utilizados por FastAPI.
"""

from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Genero(str, Enum):
    """
    Enum que representa el género de un usuario.
    """

    MASCULINO = "masculino"
    FEMENINO = "femenino"
    OTRO = "otro"


class Role(str, Enum):
    """
    Enum que representa los roles de un usuario.
    """

    ADMIN = "admin"
    USER = "user"


class Usuario(BaseModel):
    """
    Modelo Pydantic que representa un usuario del sistema.
    """

    id: UUID | None = None
    primer_nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
