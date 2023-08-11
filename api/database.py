import sqlite3
# si la base de datos no existe se crea
conn = sqlite3.connect("prueba.db")
# creamos un cursor para interactuar
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER
               )''')

conn.commit()
conn.close()

conn = sqlite3.connect("prueba.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES (?, ?)", ("Juan",21))

conn.commit()
conn.close()