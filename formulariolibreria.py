import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import libreria
import CRlib

# Asegura que la base esté creada
CRlib.crear_base_datos()

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Libros")
ventana.geometry("600x400")

# Etiquetas y entradas
tk.Label(ventana, text="Título:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(ventana, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(ventana, text="Año:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(ventana, text="Género:").grid(row=3, column=0, padx=5, pady=5)

titulo_var = tk.StringVar()
autor_var = tk.StringVar()
anio_var = tk.StringVar()
genero_var = tk.StringVar()

tk.Entry(ventana, textvariable=titulo_var).grid(row=0, column=1)
tk.Entry(ventana, textvariable=autor_var).grid(row=1, column=1)
tk.Entry(ventana, textvariable=anio_var).grid(row=2, column=1)
tk.Entry(ventana, textvariable=genero_var).grid(row=3, column=1)

# Tabla para mostrar los libros
tabla = ttk.Treeview(ventana, columns=("ID", "Título", "Autor", "Año", "Género"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Título", text="Título")
tabla.heading("Autor", text="Autor")
tabla.heading("Año", text="Año")
tabla.heading("Género", text="Género")
tabla.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

def limpiar_campos():
    titulo_var.set("")
    autor_var.set("")
    anio_var.set("")
    genero_var.set("")

def cargar_libros():
    for fila in tabla.get_children():
        tabla.delete(fila)
    for libro in libreria.obtener_libros():
        tabla.insert("", "end", values=libro)

def agregar():
    if not titulo_var.get() or not autor_var.get():
        messagebox.showwarning("Advertencia", "El título y el autor son obligatorios.")
        return
    libreria.agregar_libro(titulo_var.get(), autor_var.get(), anio_var.get(), genero_var.get())
    cargar_libros()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Libro agregado correctamente.")

def seleccionar(event):
    item = tabla.focus()
    if not item:
        return
    datos = tabla.item(item, "values")
    titulo_var.set(datos[1])
    autor_var.set(datos[2])
    anio_var.set(datos[3])
    genero_var.set(datos[4])

def actualizar():
    item = tabla.focus()
    if not item:
        messagebox.showwarning("Advertencia", "Seleccione un libro para actualizar.")
        return
    id_libro = tabla.item(item, "values")[0]
    libreria.actualizar_libro(id_libro, titulo_var.get(), autor_var.get(), anio_var.get(), genero_var.get())
    cargar_libros()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Libro actualizado correctamente.")

def eliminar():
    item = tabla.focus()
    if not item:
        messagebox.showwarning("Advertencia", "Seleccione un libro para eliminar.")
        return
    id_libro = tabla.item(item, "values")[0]
    libreria.eliminar_libro(id_libro)
    cargar_libros()
    limpiar_campos()
    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")

tabla.bind("<ButtonRelease-1>", seleccionar)

# Botones
tk.Button(ventana, text="Agregar", command=agregar).grid(row=4, column=0, pady=10)
tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=4, column=1)
tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=4, column=2)
tk.Button(ventana, text="Mostrar Libros", command=cargar_libros).grid(row=4, column=3)

cargar_libros()
ventana.mainloop()
