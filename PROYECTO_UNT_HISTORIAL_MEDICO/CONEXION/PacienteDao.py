from CONEXION.conexion import ConexionDB
from tkinter import messagebox # para mostrar ventanas emergentes


##################### FUNCIONES QUE VINCULAN A SQLITE ########################################

#::::::::::::: GUARDAR PACIENTE ::::::::::::::::::::::::::::::::::::

def guardarDatoPaciente(persona): # creamos la función guardarDatoPaciente para guardar datos en la clase DatosPaciente
    conexion = ConexionDB() # hacemos uso de la clase conexionDB para poder insertar los datos
    sql = f"""INSERT INTO DatosPaciente (NombreCompleto, ApellidosCompletos, DNI, FechaNacimiento, Edad, NumeroTelefonico, CorreoElectronico, activo) VALUES 
            ("{persona.NombreCompleto}","{persona.ApellidosCompletos}", "{persona.DNI}", "{persona.FechaNacimiento}", "{persona.Edad}","{persona.NumeroTelefonico}","{persona.CorreoElectronico}",1)"""
    
    conexion.cursor.execute(sql)
    conexion.cerrarConexion()
    titulo = "Registrar Paciente"
    mensaje = "Paciente Registrado Exitosamente"
    messagebox.showinfo(titulo, mensaje) # ventana emergente para indicar proceso completado


################### CLASE DatosPaciente ################################3

class DatosPaciente: # Creamos la clase de la tabla DatosPaciente
    def __init__(self, NombreCompleto, ApellidosCompletos, DNI, FechaNacimiento, Edad, NumeroTelefonico, CorreoElectronico): # Recibe como variables los nombres de las columnas de la Tabla DatosPaciente
        self.idPersona = None
        self.NombreCompleto = NombreCompleto
        self.ApellidosCompletos = ApellidosCompletos
        self.DNI = DNI
        self.FechaNacimiento = FechaNacimiento
        self.Edad = Edad
        self.NumeroTelefonico = NumeroTelefonico
        self.CorreoElectronico = CorreoElectronico

    def __str__(self): # Mostramos los objetos
        return f"DatosPaciente[{self.NombreCompleto},{self.ApellidosCompletos}, {self.DNI}, {self.FechaNacimiento},{self.Edad},{self.NumeroTelefonico},{self.CorreoElectronico}]"

######################################################################################
