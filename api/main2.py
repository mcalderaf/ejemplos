from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
async def index():
    return {"message": "Hello Word"}

@app.get("/libros/{id}")
async def mostrar_libro(id: int):
    return {"data": id}

@app.post("/libros/")
async def insertar_libro(libro: Libro):
    return {'message': f"Libro: {Libro.titulo} insertado correctamente"}