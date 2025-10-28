import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect("libreria.db")

# Crear nuevo libro
def agregar_libro(titulo, autor, anio, genero):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, anio, genero) VALUES (?, ?, ?, ?)",
                   (titulo, autor, anio, genero))
    con.commit()
    con.close()

# Mostrar todos los libros
def obtener_libros():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM libros")
    datos = cursor.fetchall()
    con.close()
    return datos

# Actualizar libro existente
def actualizar_libro(id_libro, titulo, autor, anio, genero):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        UPDATE libros SET titulo=?, autor=?, anio=?, genero=? WHERE id=?
    """, (titulo, autor, anio, genero, id_libro))
    con.commit()
    con.close()

# Eliminar libro
def eliminar_libro(id_libro):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id_libro,))
    con.commit()
    con.close()
