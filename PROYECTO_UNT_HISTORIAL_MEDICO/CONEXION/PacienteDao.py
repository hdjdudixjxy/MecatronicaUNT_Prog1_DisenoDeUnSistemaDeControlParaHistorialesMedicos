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

#::::::::::::::::::::::: ELIMINAR PACIENTE :::::::::::::::::::::::::::::::::::::::

def eliminarPaciente(idPersona): # creamos la función eliminarPaciente para no eliminar sus adtos de la base de datos, sino solo volverlo inactivo
    conexion = ConexionDB()
    sql = f"""UPDATE DatosPaciente SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Eliminar Paciente"
        mensaje = "Paciente eliminado exitosamente"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Eliminar Paciente"
        mensaje = "Error al eliminar Paciente"
        messagebox.showwarning(titulo, mensaje)

#:::::::::::::::::::::::::::::: EDITAR PACIENTE ::::::::::::::::::::::::::::::::::::::

def editarDatoPaciente(persona, idPersona): # creamos la función editarDatoPaciente para sobre escribir en cada objeto persona de la clase DatosPaciente
    conexion = ConexionDB()
    sql = f"""UPDATE DatosPaciente SET NombreCompleto = "{persona.NombreCompleto}", ApellidosCompletos = "{persona.ApellidosCompletos}",
            DNI = "{persona.DNI}", FechaNacimiento = "{persona.FechaNacimiento}", Edad = "{persona.Edad}", 
            NumeroTelefonico = "{persona.NumeroTelefonico}", CorreoElectronico = "{persona.CorreoElectronico}",
            activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Editar Paciente"
        mensaje = "Paciente Editado Exitosamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Editar Paciente"
        mensaje = "Error al editar paciente"
        messagebox.showinfo(titulo, mensaje)

#::::::::::::::::::::::::: TABLA EN LA GUI :::::::::::::::::::::::::::::::::::::

def listar(): # funcion que manda los datos a la lista 
    conexion = ConexionDB()

    ListaDatosPaciente = [] # lista vacía donde se guardaran los datos para mostrarlos
    sql = "SELECT * FROM DatosPaciente WHERE activo = 1" # where es la condición para que solo se muestren los pacientes activos

    try:
        conexion.cursor.execute(sql)
        ListaDatosPaciente = conexion.cursor.fetchall() # añade todos los datos a la lista
        conexion.cerrarConexion()
    except:
        title = "Datos"
        mensaje = "Registros no existen"
        messagebox.showwarning(title, mensaje)
    return ListaDatosPaciente    

def listarCondicion(where): # función que manda los datos de la lista a la tabla en la GUI si se cumple el where
    conexion = ConexionDB()
    listaDatosPaciente = []
    sql = f"SELECT * FROM DatosPaciente {where}"

    try:
        conexion.cursor.execute(sql)
        listaDatosPaciente = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "Datos"
        mensaje = "Registros no existen"
        messagebox.showwarning(title, mensaje)
    return listaDatosPaciente

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
