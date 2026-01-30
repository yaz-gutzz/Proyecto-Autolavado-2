"""
API REST de usuarios usando FastAPI.

Permite:
- Listar usuarios
- Buscar usuarios por nombre
- Crear usuarios
- Actualizar usuarios
- Eliminar usuarios

Base de datos simulada en memoria.
"""

from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from model import Genero, Role, Usuario


app = FastAPI()


# -------------------
# Base de datos en memoria
# -------------------
db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primer_nombre="Yazmin",
        apellidos="Gutierrez",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primer_nombre="Obed",
        apellidos="Guzman",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
]


# -------------------
# Listar o buscar usuarios
# -------------------
@app.get("/api/v1/users")
async def get_users(primer_nombre: Optional[str] = None):
    """
    Listar todos los usuarios o buscar por nombre.
    """
    if primer_nombre:
        resultado = [
            usuario for usuario in db
            if usuario.primer_nombre.lower() == primer_nombre.lower()
        ]
        if not resultado:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )
        return resultado

    return db


# -------------------
# Crear usuario
# -------------------
@app.post("/api/v1/users")
async def create_user(usuario: Usuario):
    """
    Crear un nuevo usuario.
    """
    usuario.id = uuid4()
    db.append(usuario)
    return usuario


# -------------------
# Actualizar usuario
# -------------------
@app.put("/api/v1/users")
async def update_user(user_id: UUID, usuario: Usuario):
    """
    Actualizar un usuario existente por ID.
    """
    for index, usuario_db in enumerate(db):
        if usuario_db.id == user_id:
            usuario.id = user_id
            db[index] = usuario
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


# -------------------
# Eliminar usuario
# -------------------
@app.delete("/api/v1/users")
async def delete_user(user_id: UUID):
    """
    Eliminar un usuario por ID.
    """
    for index, usuario in enumerate(db):
        if usuario.id == user_id:
            usuario_eliminado = db.pop(index)
            return {
                "message": "Usuario eliminado",
                "usuario": usuario_eliminado
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
