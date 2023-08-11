import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn = sqlite3.connect("billboardi100.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS datos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               artista TEXT NOT NULL,
               posicion INTEGER
               )''')

conn.commit()
conn.close()

class Datos(BaseModel):
    titulo: str
    artista: str
    posicion: int

app = FastAPI()

@app.post("/agregar/")
async def agregar_datos(datos: Datos):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO datos (titulo, artista, posicion) VALUES (?, ?, ?)", (datos.titulo, datos.artista, datos.posicion))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

@app.get("/datos/")
async def obtener_todos_datos():
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"id": resultado[0], "titulol": resultado[1], "artista": resultado[2], "posicion": resultado[3]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

@app.get("/consultar/{id}/")
async def consultar_datos(id: int):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, artista, posicion FROM datos WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return {"titulo": resultado[0], "artista": resultado[1], "posicion": resultado[2]}
    else:
        return {"mensaje": "Dato no encontrado"}
    

@app.put("/actualizar/{id}/")
async def actualizar_datos(id:int, datos: Datos):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE datos SET titulo=?, artista=?, posicion=? WHERE id=?", (datos.titulo,datos.artista,datos.posicion))
    resultado = cursor.fetchone()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

@app.delete("/eliminar/{id}/")
async def eliminar_datos(id: int):
    conn = sqlite3.connect("billboard100.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM datos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}
