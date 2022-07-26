import tkinter as tk
import sqlite3 as sql

def main():
    base = tk.Tk() 
    base.iconbitmap("ICONO.ico") # Agregue un icono 
    base.title("HISTORIAS CLÍNICAS") 
    base.resizable(width=True, height=True) #Permite maximizar la ventana
    base.minsize(width=1000,height=800) # Tamaño mínimo

    ventana = tk.Frame(base)
    ventana.mainloop()

con=sql.connect("BaseDeDatos.db")

if __name__ == "__main__": 
    main()
