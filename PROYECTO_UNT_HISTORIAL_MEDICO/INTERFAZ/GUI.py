from CONEXION.PacienteDao import DatosPaciente, editarDatoPaciente, guardarDatoPaciente, listar, listarCondicion, eliminarPaciente 
# traemos la clase y las funciones para la persona
import tkinter as tk # Importamos la GUI TKINTER
from tkinter import W, ttk, messagebox


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
        self.tablaPaciente()

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
        self.entryApellidos = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApellidos.config(width=50, font=("verdana",15))
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

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

        #################### BUSCADOR ########################
        
        self.lblBuscarDni = tk.Label(self, text="Buscar DNI: ")
        self.lblBuscarDni.config(font=("verdana",15,"bold"), bg="lightseagreen")
        self.lblBuscarDni.grid(column=3, row=0, padx=2, pady=5)

        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=("verdana",15))
        self.entryBuscarDni.grid(column=4, row=0, padx=2, pady=5)

        self.btnBuscarCondicion = tk.Button(self, text="BUSCAR", command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=10, font=("verdana",12,"bold"), 
                                bg="purple1", cursor="hand2",activebackground="purple3")
        self.btnBuscarCondicion.grid(column=3,row=1, padx=2, pady=5)

        self.btnLimpiarBuscador = tk.Button(self, text="LIMPIAR")
        self.btnLimpiarBuscador.config(width=10, font=("verdana",12,"bold"), 
                                bg="gold", cursor="hand2",activebackground="goldenrod")
        self.btnLimpiarBuscador.grid(column=4,row=1, padx=2, pady=5)

    def buscarCondicion(self): # función para el entry buscar por dni

        if len(self.svBuscarDni.get()) > 0:
            where = "WHERE 1=1" # manda todos los valores de la base de datos

            if len(self.svBuscarDni.get()) > 0:
                where = "WHERE Dni = " + self.svBuscarDni.get() + "" 
            
                self.tablaPaciente(where) # muestra en la interfaz los datos de la persona con el dni ingresado
            else:
                self.tablaPaciente() # si no se encuentra ese where dni entonces no se mostrará nada
        else:
            if len(self.svBuscarDni.get()) == 0: # si no colocamos nada en el entry de buscar dni, nos mostrará todos los inactivos
                where = "WHERE activo = 0 "
                self.tablaPaciente(where)
            
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
        self.entryApellidos.config(state="disabled")
        self.entryDni.config(state="disabled")
        self.entryFecNacimiento.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.entryCorreo.config(state="disabled")
        self.entryTelefono.config(state="disabled")

        self.btnCancelar.config(state="disabled")
        self.btnGuardar.config(state="disabled")
    
    def habilitar(self): # esta funcion tiene la función de habilitar los entrys

        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svFecNacimiento.set("")
        self.svEdad.set("")
        self.svTelefono.set("")
        self.svCorreo.set("")

        self.entryNombre.config(state="normal")
        self.entryApellidos.config(state="normal")
        self.entryDni.config(state="normal")
        self.entryFecNacimiento.config(state="normal")
        self.entryEdad.config(state="normal")
        self.entryCorreo.config(state="normal")
        self.entryTelefono.config(state="normal")

        self.btnCancelar.config(state="normal")
        self.btnGuardar.config(state="normal")        
        
    def tablaPaciente(self, where=""): #funcion para insertar la tabla en la GUI

        if len(where) > 0:
            self.listaDatosPaciente = listarCondicion(where)
        else:
            self.listaDatosPaciente = listar()
            self.listaDatosPaciente.reverse()

        self.tabla = ttk.Treeview(self, column=("NombreCompleto", "ApellidosCompletos","DNI","FechaNacimiento","Edad","NumeroTelefonico","CorreoElectronico")) 
        #ttk.Treeview crea la tabla 
        self.tabla.grid(column=0, row=8, columnspan=5, sticky="nswe")
        
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=8, column=4, sticky="nse")
        self.tabla.config(height=15)

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure("evenrow", background="antiquewhite1") # damos color a las filas 

        #definimos los títulos de cada columna

        self.tabla.heading("#0",text="ID")
        self.tabla.heading("#1",text="Nombres")
        self.tabla.heading("#2",text="Apellidos")
        self.tabla.heading("#3",text="DNI")
        self.tabla.heading("#4",text="F. Nacimiento")
        self.tabla.heading("#5",text="Edad")
        self.tabla.heading("#6",text="Telefono")
        self.tabla.heading("#7",text="Correo")

        self.tabla.column("#0", anchor=W, width=3)
        self.tabla.column("#1", anchor=W, width=120)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=20)
        self.tabla.column("#4", anchor=W, width=100)
        self.tabla.column("#5", anchor=W, width=3)
        self.tabla.column("#6", anchor=W, width=40)
        self.tabla.column("#7", anchor=W, width=120)

        for p in self.listaDatosPaciente:
            self.tabla.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7]), tags=("evenrow",)) # con tags referenciamos el tag configure que hicimos anteriormente

        # Creamos los nuevos botones debajo de la tabla

        self.btnEditarPaciente = tk.Button(self, text="Editar Paciente", command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=("verdana",12,"bold"), bg="orange", activebackground="darkorange", cursor="hand2")
        self.btnEditarPaciente.grid(row=9, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text="Eliminar Paciente", command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=("verdana",12,"bold"), bg="cornflowerblue", activebackground="royalblue2", cursor="hand2")
        self.btnEliminarPaciente.grid(row=9, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text="Historial Paciente")
        self.btnHistorialPaciente.config(width=50,font=("verdana",12,"bold"), bg="cyan2", activebackground="cyan3", cursor="hand2")
        self.btnHistorialPaciente.grid(row=9, column=2, columnspan=3, pady=5)


    ################ FUNCIONES QUE VINCULAN LOS OBJETOS ###############################

    def guardarPaciente(self): # función para insertar los datos del paciente a la base de datos
        persona = DatosPaciente(self.svNombre.get(), self.svApellidos.get(), self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(),self.svTelefono.get(), self.svCorreo.get())
        # el metodo get lee lo que se inserta en los entrys

        if self.idPersona == None: # si el id no tiene valor, entonces guarda el dato, sino solo lo vamos a editar
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        self.deshabilitar() # una vez presionado el boton duardar, se va a borrar todos los datos de los entrys
        self.tablaPaciente() # para actualizar la tabla cuando se ingresan datos
    
    def editarPaciente(self): # funcion que cambia los datos, pero en la tabla de la GUI
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"] #Trae el ID
            self.NombrePaciente = self.tabla.item(self.tabla.selection())["values"][0] # agrega los datos de el objeto ya insertado a uno nuevo, para poder editarlo
            self.ApellidosPaciente = self.tabla.item(self.tabla.selection())["values"][1]
            self.DNIPaciente = self.tabla.item(self.tabla.selection())["values"][2]
            self.FecNacimientoPaciente = self.tabla.item(self.tabla.selection())["values"][3]
            self.EdadPaciente = self.tabla.item(self.tabla.selection())["values"][4]
            self.TelefonoPaciente = self.tabla.item(self.tabla.selection())["values"][5]
            self.CorreoPaciente = self.tabla.item(self.tabla.selection())["values"][6]

            self.habilitar()

            self.entryNombre.insert(0, self.NombrePaciente) # con el metodo insert, hacemos que aparezcan los datos ya puestos en la tabla, en cada entry
            self.entryApellidos.insert(0, self.ApellidosPaciente)
            self.entryDni.insert(0, self.DNIPaciente)
            self.entryFecNacimiento.insert(0, self.FecNacimientoPaciente)
            self.entryEdad.insert(0, self.EdadPaciente)
            self.entryTelefono.insert(0,self.TelefonoPaciente)
            self.entryCorreo.insert(0,self.CorreoPaciente)
            
        except:
            title = "Editar Paciente"
            mensaje = "Error al editar paciente"
            messagebox.showerror(title, mensaje)  

    def eliminarDatoPaciente(self): 
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"]
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = "Eliminar Paciente"
            mensaje = "No se pudo eliminar paciente"
            messagebox.showinfo(title, mensaje)  

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