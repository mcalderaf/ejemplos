from fastapi import FastAPI


app = FastAPI()
# creamos una ruta para acceder a un cierrto valor
@app.get("/")
def raiz():
    return {"Hello": "Word"}

@app.get("/items/{item_id}/{m}")
def read_item(item_id: int, m: str = None):
    return {"item_id": item_id, "m": m}
