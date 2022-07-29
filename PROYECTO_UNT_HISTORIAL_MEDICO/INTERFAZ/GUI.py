import tkinter as tk # Importamos la GUI TKINTER
from CONEXION.PacienteDao import DatosPaciente, guardarDatoPaciente, eliminarPaciente, editarDatoPaciente # traemos la clase y las funciones para la persona

######################### VENTANA DE FONDO ###################

class Frame(tk.Frame): # clase ventana
    def __init__(self, aplicacion): 

        super().__init__(aplicacion) # utilizamos super() para llevar a cabo herencias múltiples, de las subclases a la superclase
        self.aplicacion = aplicacion
        self.pack(fill=tk.BOTH, expand=True)
        self.config(bg="lightseagreen")
        self.idPersona = None # los id, los utilizaremos para aplicar condiciones
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None
        self.idHistoriaMedicaEditar = None
        self.camposPaciente()
        self.deshabilitar()

    def camposPaciente(self):

        ##################### LABELS ##########################

        self.lblNombre = tk.Label(self, text="NOMBRE COMPLETO: ")
        self.lblNombre.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w") # Preguntar como hacerlo hacia la izquierda con el metodo grid
        self.lblNombre.grid(column=0, row=0, pady=5)

        self.lblApellidos = tk.Label(self, text="APELLIDOS COMPLETOS: ")
        self.lblApellidos.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblApellidos.grid(column=0,row=1, pady=5)

        self.lblDni = tk.Label(self, text="DNI: ")
        self.lblDni.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblDni.grid(column=0,row=2, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text="FECHA DE NACIMIENTO: ")
        self.lblFechNacimiento.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblFechNacimiento.grid(column=0,row=3, pady=5)

        self.lblEdad = tk.Label(self, text="EDAD: ")
        self.lblEdad.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblEdad.grid(column=0,row=4, pady=5)

        self.lblTelefono = tk.Label(self, text="TELÉFONO: ")
        self.lblTelefono.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblTelefono.grid(column=0,row=5, pady=5) 

        self.lblCorreo = tk.Label(self, text="CORREO ELECTRÓNICO: ")
        self.lblCorreo.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblCorreo.grid(column=0,row=6, pady=5)

        ################## ENTRYS ###############################

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=("verdana",15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellidos = tk.StringVar()
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApePaterno.config(width=50, font=("verdana",15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=("verdana",15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=("verdana",15))
        self.entryFecNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=("verdana",15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=("verdana",15))
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=("verdana",15))
        self.entryCorreo.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        ######################### BUTTONS ####################################

        self.btnNuevo = tk.Button(self, text="NUEVO", command=self.habilitar)
        self.btnNuevo.config(width=20, font=("verdana",12,"bold"), 
                                background="firebrick1", cursor="hand2",activebackground="firebrick3")
        self.btnNuevo.grid(column=0,row=7, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text="GUARDAR", command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=("verdana",12,"bold"), 
                                background="sienna1", cursor="hand2",activebackground="sienna3")
        self.btnGuardar.grid(column=1,row=7, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text="CANCELAR")
        self.btnCancelar.config(width=20, font=("verdana",12,"bold"), 
                                background="khaki1", cursor="hand2",activebackground="khaki3")
        self.btnCancelar.grid(column=2,row=7, padx=10, pady=5)


    def deshabilitar(self): # esta funcion tiene la finalidad de bloquear los entrys, para que luego con el botón Nuevo, los entry se habiliten
    
        self.idPersona = None
        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svFecNacimiento.set("")
        self.svEdad.set("")
        self.svTelefono.set("")
        self.svCorreo.set("")

        self.entryNombre.config(state="disabled")
        self.entryApePaterno.config(state="disabled")
        self.entryDni.config(state="disabled")
        self.entryFecNacimiento.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.entryCorreo.config(state="disabled")
        self.entryTelefono.config(state="disabled")

        self.btnCancelar.config(state="disabled")
        self.btnGuardar.config(state="disabled")
    
    def habilitar(self): # esta funcion tiene la función de habilitar los entrys

        self.idPersona = None
        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svFecNacimiento.set("")
        self.svEdad.set("")
        self.svTelefono.set("")
        self.svCorreo.set("")

        self.entryNombre.config(state="normal")
        self.entryApePaterno.config(state="normal")
        self.entryDni.config(state="normal")
        self.entryFecNacimiento.config(state="normal")
        self.entryEdad.config(state="normal")
        self.entryCorreo.config(state="normal")
        self.entryTelefono.config(state="normal")

        self.btnCancelar.config(state="normal")
        self.btnGuardar.config(state="normal")        
        



    ################ FUNCIONES QUE VINCULAN LOS OBJETOS ###############################

    def guardarPaciente(self): #
        persona = DatosPaciente(self.svNombre.get(), self.svApellidos.get(), self.svFecNacimiento.get(),self.svDni.get(), self.svEdad.get(),self.svTelefono.get(), self.svCorreo.get())
        # el metodo get lee lo que se inserta en los entrys
        # if self.idPersona == None:
        guardarDatoPaciente(persona)
        self.deshabilitar() # una vez presionado el boton duardar, se va a borrar todos los datos de los entrys























######################## ERROR INTERFAZ ##########################

def error():

    AppError = tk.Tk()
    AppError.title("¡Vaya!")
    AppError.geometry("350x200+600+200") # resolución por defecto
    AppError.iconbitmap("ICONOS/error2.ico")
    AppError.resizable(width=False, height=False) # ponemos que se pueda agrandar?
    AppError.configure(background="steelblue1")

###################################################

    LbError = tk.Label(AppError,
        text="HA OCURRIDO UN ERROR",
        font=("Arial", 18, "bold"),
        foreground="red2",
        background="steelblue1"
    )

    LbError.place(x=25, y=60)

############################################################

    LbError2 = tk.Label(AppError,
        text="Vuelva a ejecutar la aplicación",
        font=("Arial", 12),
        foreground="gray30",
        background="steelblue1"
    )

    LbError2.place(x=74, y=97)

###############################################################

    AppError.mainloop()








