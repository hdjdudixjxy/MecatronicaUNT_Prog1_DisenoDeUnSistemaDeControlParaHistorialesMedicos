import sqlite3

class ConexionDB:
    def __init__(self):
        self.baseDatos = "BaseDeDatos/DbHistorial.db" # insertamos la ruta
        self.conexion = sqlite3.connect(self.baseDatos) # nos conectamos a la baase de datos
        self.cursor = self.conexion.cursor() # el metodo cursor nos permite modificar datos

    def cerrarConexion(self):
        self.conexion.commit() # subimos los datos insertados en los entrys
        self.conexion.close() # cerramos la conexión