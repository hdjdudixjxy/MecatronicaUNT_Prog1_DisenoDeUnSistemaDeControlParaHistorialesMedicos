from .enlaceDB import enlace
from tkinter import messagebox # Queremos solo la caja emergente de mensaje, no otras etiquetas

#################### FUNCION QUE GUARDA DATOS DEL PACIENTE ################################333333

def GuardarDPaciente(persona):
    conexion=enlace()
    sql = f"""insert into DatosPaciente (Nombre,Apellido,DNI,Edad,Fnacimiento,Ntelefonico,Celectronico,activo) values 
    ('{persona.Nombre}','{persona.Apellido}','{persona.DNI}','{persona.Edad}','{persona.Fnacimiento}','{persona.Ntelefonico}',
    '{persona.Celectronico}',1) """
    try:
        conexion.cursor.execute(sql)
        conexion.CerrarConexion()
        title = "Registrar Paciente"
        mensaje = "Paciente Registrado"
        messagebox.showinfo(title,mensaje)
    except:
        title = "Registrar Paciente"
        mensaje = "Error al registrar el paciente"
        messagebox.showerror(title,mensaje)

########################### FUNCION PARA BUSCAR CON EL DNI #########################

def listarCondicion(where):
    conexion=enlace()
    listConP=[]
    sql=f"select * from  DatosPersona {where}"

    try:
        conexion.cursor.execute(sql)
        listConP=conexion.cursor.fetchall()
        conexion.CerrarConexion
    except:
        title="DATOS"
        mensaje="No exite ese registro"
        messagebox.showwarning(title,mensaje)        

########################### FUNCION PARA ELIMINAR PACIENTE DEL REGISTRO ####################333

def eliminarPaciente(idPersona):
    conexion=enlace()
    sql=f"""update DatosPersona set activo = 0 where idPersona={idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.CerrarConexion
        title="ELIMINAR PACIENTE"
        mensaje="Eliminado satisfactoriamente"
        messagebox.showwarning(title,mensaje)        
    except:
        title="ELIMINAR PACIENTE"
        mensaje="Error al eliminar paciente"
        messagebox.showwarning(title,mensaje)  

######################## FUNCION MOSTRAR PACIENTE ############################

def mostarP():
    conexion = enlace ()
    listaPersona=[]
    sql="select * from DatosPersona where activo = 1"

    try: 
        conexion.cursor.execute(sql)
        listaPersona=conexion.cursor.fetchall()
        conexion.CerrarConexion
    except:
        title="datos"
        mensaje="No exite ese registro"
        messagebox.showwarning(title,mensaje)

####################################### OBJETO PERSONA ##################################################

class Persona: 
    def __init__(self,Nombre, Apellido, DNI, Edad, Fnacimiento, Ntelefonico, Celectronico): # __init__ método que crea atributos a un objeto
        self.idPersona=None
        self.Nombre=Nombre
        self.Apellido=Apellido
        self.DNI=DNI
        self.Edad=Edad
        self.Fnacimiento=Fnacimiento
        self.Ntelefonico=Ntelefonico
        self.Celectronico=Celectronico

    def __str__(self): # __str__ método para imprimir atributos de un objeto
        return f"Persona[{self.Nombre},{self.Apellido},{self.DNI},{self.Edad},{self.Fnacimiento},{self.Ntelefonico},{self.Celectronico}]"












