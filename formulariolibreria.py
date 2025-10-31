
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import libreria

class FormularioLibreria:
    def __init__(self):
        self.libreria1 = libreria.Libreria()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Gestor de Libros con Tkinter y SQLite")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.form_agregar()
        self.form_listar()
        self.form_borrar()
        self.form_actualizar()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    # ---------------- AGREGAR LIBROS ----------------
    def form_agregar(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Agregar Libro")

        frame = ttk.LabelFrame(self.pagina1, text="Datos del Libro")
        frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(frame, text="Título:").grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(frame, text="Autor:").grid(column=0, row=1, padx=5, pady=5)
        ttk.Label(frame, text="Año:").grid(column=0, row=2, padx=5, pady=5)
        ttk.Label(frame, text="Género:").grid(column=0, row=3, padx=5, pady=5)

        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.anio = tk.StringVar()
        self.genero = tk.StringVar()

        ttk.Entry(frame, textvariable=self.titulo, width=30).grid(column=1, row=0)
        ttk.Entry(frame, textvariable=self.autor, width=30).grid(column=1, row=1)
        ttk.Entry(frame, textvariable=self.anio, width=30).grid(column=1, row=2)
        ttk.Entry(frame, textvariable=self.genero, width=30).grid(column=1, row=3)

        ttk.Button(frame, text="Agregar", command=self.agregar_libro).grid(column=1, row=4, pady=10)

    def agregar_libro(self):
        datos = (self.titulo.get(), self.autor.get(), self.anio.get(), self.genero.get())
        if "" in datos:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return
        self.libreria1.alta(datos)
        messagebox.showinfo("Éxito", "Libro agregado correctamente")
        self.titulo.set(""); self.autor.set(""); self.anio.set(""); self.genero.set("")

    # ---------------- LISTAR LIBROS ----------------
    def form_listar(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Listado de Libros")

        frame = ttk.LabelFrame(self.pagina2, text="Libros guardados")
        frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Button(frame, text="Mostrar Libros", command=self.listar_libros).grid(column=0, row=0, pady=5)
        self.texto_listado = scrolledtext.ScrolledText(frame, width=50, height=15)
        self.texto_listado.grid(column=0, row=1, padx=5, pady=5)

    def listar_libros(self):
        self.texto_listado.delete("1.0", tk.END)
        libros = self.libreria1.recuperar_todos()
        for libro in libros:
            self.texto_listado.insert(tk.END, f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]} | Género: {libro[4]}\n")

    # ---------------- BORRAR LIBRO ----------------
    def form_borrar(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrar Libro")

        frame = ttk.LabelFrame(self.pagina3, text="Eliminar por ID")
        frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(frame, text="ID del libro:").grid(column=0, row=0, padx=5, pady=5)
        self.id_borrar = tk.StringVar()
        ttk.Entry(frame, textvariable=self.id_borrar, width=10).grid(column=1, row=0, padx=5, pady=5)

        ttk.Button(frame, text="Borrar", command=self.borrar_libro).grid(column=1, row=1, pady=10)

    def borrar_libro(self):
        if not self.id_borrar.get().isdigit():
            messagebox.showwarning("Error", "Debe ingresar un ID válido")
            return
        self.libreria1.baja(int(self.id_borrar.get()))
        messagebox.showinfo("Éxito", "Libro eliminado correctamente")
        self.id_borrar.set("")

    # ---------------- ACTUALIZAR LIBRO ----------------
    def form_actualizar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Actualizar Libro")

        frame = ttk.LabelFrame(self.pagina4, text="Actualizar datos por ID")
        frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(frame, text="ID:").grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(frame, text="Nuevo Título:").grid(column=0, row=1, padx=5, pady=5)
        ttk.Label(frame, text="Nuevo Autor:").grid(column=0, row=2, padx=5, pady=5)
        ttk.Label(frame, text="Nuevo Año:").grid(column=0, row=3, padx=5, pady=5)
        ttk.Label(frame, text="Nuevo Género:").grid(column=0, row=4, padx=5, pady=5)

        self.id_actualizar = tk.StringVar()
        self.titulo_nuevo = tk.StringVar()
        self.autor_nuevo = tk.StringVar()
        self.anio_nuevo = tk.StringVar()
        self.genero_nuevo = tk.StringVar()

        ttk.Entry(frame, textvariable=self.id_actualizar, width=10).grid(column=1, row=0)
        ttk.Entry(frame, textvariable=self.titulo_nuevo, width=30).grid(column=1, row=1)
        ttk.Entry(frame, textvariable=self.autor_nuevo, width=30).grid(column=1, row=2)
        ttk.Entry(frame, textvariable=self.anio_nuevo, width=30).grid(column=1, row=3)
        ttk.Entry(frame, textvariable=self.genero_nuevo, width=30).grid(column=1, row=4)

        ttk.Button(frame, text="Actualizar", command=self.actualizar_libro).grid(column=1, row=5, pady=10)

    def actualizar_libro(self):
        if not self.id_actualizar.get().isdigit():
            messagebox.showwarning("Error", "Debe ingresar un ID válido")
            return
        datos = (
            self.titulo_nuevo.get(),
            self.autor_nuevo.get(),
            self.anio_nuevo.get(),
            self.genero_nuevo.get(),
            int(self.id_actualizar.get())
        )
        self.libreria1.actualizar(datos)
        messagebox.showinfo("Éxito", "Libro actualizado correctamente")
        self.id_actualizar.set(""); self.titulo_nuevo.set(""); self.autor_nuevo.set("")
        self.anio_nuevo.set(""); self.genero_nuevo.set("")


if __name__ == "__main__":
    FormularioLibreria()