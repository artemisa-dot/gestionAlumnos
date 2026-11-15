import sqlite3

# Conexión a tu base de datos local actual
conn = sqlite3.connect("atemisa.db")

print("Generando volcado de la base de datos...")
with open("dump.sql", "w", encoding="utf-8") as f:
    for linea in conn.iterdump():
        f.write(f"{linea}\n")

conn.close()
print("¡Listo! Se ha creado el archivo 'dump.sql' en tu carpeta.")