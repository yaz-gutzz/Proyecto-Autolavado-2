from fastapi import FastAPI, HTTPException
from typing import List, Optional
from uuid import UUID, uuid4
from model import Genero, Role, Usuario

app = FastAPI()

# Base de datos en memoria
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

# -------------------------------
# Endpoints de usuario
# -------------------------------

@app.get("/api/v1/users")
async def get_users(primerNombre: Optional[str] = None):
    """
    Lista todos los usuarios o busca por nombre si se pasa el parámetro 'primerNombre'.
    """
    if primerNombre:
        resultado = [user for user in db if user.primerNombre.lower() == primerNombre.lower()]
        if not resultado:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return resultado
    return db

@app.post("/api/v1/users")
async def create_user(usuario: Usuario):
    """
    Crear un nuevo usuario.
    """
    usuario.id = uuid4()  
    db.append(usuario)
    return usuario

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, usuario: Usuario):
    """
    Actualizar un usuario existente por ID.
    """
    for index, u in enumerate(db):
        if u.id == user_id:
            usuario.id = user_id  # Mantener el mismo ID
            db[index] = usuario
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """
    Eliminar un usuario por ID.
    """
    for index, u in enumerate(db):
        if u.id == user_id:
            deleted_user = db.pop(index)
            return {"message": "Usuario eliminado", "usuario": deleted_user}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
