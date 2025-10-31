import sqlite3

class Libreria:
    def __init__(self):
        self.conexion = sqlite3.connect("libros.db")
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                anio TEXT NOT NULL,
                genero TEXT NOT NULL
            )
        ''')
        self.conexion.commit()

    def alta(self, datos):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO libros (titulo, autor, anio, genero) VALUES (?, ?, ?, ?)", datos)
        self.conexion.commit()

    def recuperar_todos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        return cursor.fetchall()

    def baja(self, id_libro):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id=?", (id_libro,))
        self.conexion.commit()

    def actualizar(self, datos):
        cursor = self.conexion.cursor()
        cursor.execute("""
            UPDATE libros
            SET titulo=?, autor=?, anio=?, genero=?
            WHERE id=?
        """, datos)
        self.conexion.commit()