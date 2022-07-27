import sqlite3 as sql

class enlace:
    def __init__(self): # Self le da atributos a la clase enlace
        self.conexion=sql.connect("BaseDeDatos/BaseDeDatos.db")
        self.cursor=self.conexion.cursor() # Metodo para editar datos

    def CerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()



