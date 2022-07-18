import tkinter as tk
import sqlite3 as sql

def main():
    base = tk.Tk()
    base.title("HISTORIAS CLÍNICAS")
    base.resizable()
    
    base.mainloop()

con=sql.connect("BaseDeDatos.db")

if __name__ == "__main__":
    main()
