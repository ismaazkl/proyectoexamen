import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st 
import libreria
class FormularioLibreria:
    def __init__(self):
        self.Libreria1=libreria.Libreria()
        self.ventana1= tk.Tk()
        self.ventana1.title("Formulario Libreria")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.Agregar_libros()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop
        
        
        
        

    def carga_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text= "Agregar en mis libros")               
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="Agregar")
        self.label1=ttk.Label(self.labelframe1,text="Titulo del libro")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.titulocarga=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulocarga)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)

        self.label1=ttk.Label(self.labelframe1,text="Autor")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.autorcarga=tk.StringVar()
        self.entryautor=ttk.Entry(self.labelframe1, textvariable=self.autorcarga)
        self.entryautor.grid(column=1, row=0, padx=4, pady=5)

        self.label1=ttk.Label(self.labelframe1,text="Año de Publicacion")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.aniocarga=tk.StringVar()
        self.entryanio=ttk.Entry(self.labelframe1, textvariable=self.aniocarga)
        self.entryanio.grid(column=1, row=0, padx=4, pady=6)

        self.label1=ttk.Label(self.labelframe1,text="Genero")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.generocarga=tk.StringVar()
        self.entrygenero=ttk.Entry(self.labelframe1, textvariable=self.generocarga)
        self.entrygenero.grid(column=1, row=0, padx=4, pady=7)

        
        
    def agregar(self):
        datos=(self.autorcarga.get(), self.titulocarga.get(),self.aniocarga.get(),self.generocarga.get())
        self.libreria1.alta(datos)
        mb.showinfo("!!Noticia!!","Los datos el libro fueron cargados")
        self.titulocarga.set("")
        self.autorcarga.set("")
        self.aniocarga.set("")
        self.generocarga.set("")
    
    def listado(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Listado completo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text=("Libros"))
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe2,text="Listado Completo",command=self.listar)
        self.boton1.grind(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe2, width=40, height=10)
    
    def listar(self):
        respuesta=self.libreria1.recuperar_todos()
        self.scrolledtext.delete("1,0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END,"codigo:"+str(fila[0])+"\nTitulo:"+fila[1]+"\nAutor:"+str(fila[2])+"\nAño de publicacion:"+str(fila[4])+"\nGenero:"+str(fila[6])+"\n\n")

    def borrado_de_articulos(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrado de artículos")
        self.labelframe3=ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.borrador=tk.StringVar()
        self.borrador=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.borrador.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar artículo", command=self.borrar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
    def borrar(self):
        datos=(self.autorcarga.get(), self.titulocarga.get(),self.aniocarga.get(),self.generocarga.get())
        self.Libreria1.baja(datos)
        mb.showinfo("Información", "El artículo fue borrado")
        
        self.autorcarga.set("")
        self.titulocarga.set("")
        self.aniocarga.set("")
        self.generocarga.set("")


    def Agregar_libros(self):
        self.carga_articulos()
        self.listado()
        self.borrado_de_articulos()


if __name__ == "__main__":
    formulario=FormularioLibreria()
