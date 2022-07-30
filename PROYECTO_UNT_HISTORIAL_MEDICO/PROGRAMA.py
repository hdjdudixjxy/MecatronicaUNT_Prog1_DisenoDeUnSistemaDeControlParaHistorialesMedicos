import tkinter as tk
from INTERFAZ.GUI import Frame
from INTERFAZ.GUI import error

def main():
    aplicacion = tk.Tk() # interfaz principal
    aplicacion.title("HISTORIAS CLINICAS") # nombre de la interfaz
    aplicacion.resizable(width=False, height=False) # expansión a pantalla completa
    aplicacion.geometry("1420x720+40+40") # tamaño por defecto y posición
    aplicacion.minsize(width=1280, height=720) # tamaño mínimo al minimizar
    aplicacion.iconbitmap("ICONOS/ICONO.ico") # icono de la interfaz
    fondo = Frame(aplicacion) # ventana para dar color de fondo
    fondo.mainloop() # bucle generador
try:
    if __name__ == "__main__":
        main()
except:
    error()

#### VARIABLE-LEYENDA #######
# lbl"..." : significa Label
# sv "..." : es la variable de los entrys
# entry "..." : significa entry
# btn "..." : significa button








