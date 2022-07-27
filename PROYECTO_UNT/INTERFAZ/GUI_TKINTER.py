import tkinter as tk
from tkinter import ttk
import datetime as dt
from EnlaceSQLPy.PacienteDao import Persona, listarCondicion, mostarP


def interfaz():
    
    aplicacion = tk.Tk()
    aplicacion.title("HISTORIAS CLINICAS")
    aplicacion.geometry("1366x768+100+20") # resolución por defecto
    aplicacion.iconbitmap("ICONO.ico")
    aplicacion.resizable(width=True, height=True) # ponemos que se pueda agrandar?
    aplicacion.configure(background="lightseagreen")
    idPersona=None


    #############################################################

    ventana1=tk.Frame(aplicacion,
        background="steelblue",
    )

    ventana1.pack(fill=tk.X)

    NomClinica = tk.Label(ventana1,
        text="MEDICLINIC",
        font=("Verdana", 22, "bold", "underline"),
        background="steelblue"
    )

    fec=tk.Label(ventana1,
        text=dt.date.today(),
        font = ("Verdana", 12),
        relief = tk.SUNKEN,
        border=4
    )

    fec.pack(side=tk.RIGHT, padx=5, pady=7)
    NomClinica.place(relx=0.4)

    #################################################
    ventana2=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana2.pack(fill=tk.X)

    ventana2_1=tk.Frame(ventana2,
        background = "lightseagreen"
        )

    ventana2_2=tk.Frame(ventana2,
    background = "lightseagreen"
    )

    ventana2_2.pack(side=tk.RIGHT, padx=50)

    ventana2_1.place(relx=0.1)

    LbNombre = tk.Label(ventana2_1,
        text="NOMBRE COMPLETO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VNombre=tk.StringVar()
    EnNombre=tk.Entry(ventana2_1,
        textvariable = VNombre,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnNombre.pack(side=tk.RIGHT,padx=40, pady=7)

    LbNombre.pack(side=tk.RIGHT, padx=10, pady=7)

    LbBDNI_BUSCAR = tk.Label(ventana2_2,
        text="BUSCAR POR DNI: ",
        font = ("Verdana", 16),
        background = "lightseagreen"
    )

    VBDNI=tk.IntVar()
    EnBDNI_BUSCAR=tk.Entry(ventana2_2,
        textvariable=VBDNI,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=10
    )

    EnBDNI_BUSCAR.pack(side=tk.RIGHT)

    LbBDNI_BUSCAR.pack(side=tk.RIGHT, padx=10)

    #################################################

    ventana3=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana3.pack(fill=tk.X)

    ventana3_1=tk.Frame(ventana3,
        background = "lightseagreen"
        )

    ventana3_2=tk.Frame(ventana3,
    background = "lightseagreen"
    )

    ventana3_2.pack(side=tk.RIGHT, padx=50)

    ventana3_1.place(relx=0.1)


    LbApellido = tk.Label(ventana3_1,
        text="APELLIDOS COMPLETOS: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VApellido=tk.StringVar() # StringVAR PERMITE ADMINISTRAR DATOS DE LA ENTRADA DE TIPO VARIABLE STRING
    EnApellido=tk.Entry(ventana3_1,
        textvariable = VApellido,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnApellido.pack(side=tk.RIGHT,pady=20)

    LbApellido.pack(side=tk.RIGHT, padx=10, pady=20)

    BtDNI_Buscar = tk.Button(ventana3_2,
        text="BUSCAR",
        font = ("Verdana", 16),
        background = "khaki1",
        relief = tk.GROOVE,
        border=5,
        width=8
    )

    BtDNI_Limpiar = tk.Button(ventana3_2,
        text="LIMPIAR",
        font = ("Verdana", 16),
        background = "khaki1",
        relief = tk.GROOVE,
        border=5,
        width=8
    )

    BtDNI_Limpiar.pack(side=tk.RIGHT, pady=10)

    BtDNI_Buscar.pack(side=tk.RIGHT, padx=10, pady=10)

    #################################################

    ventana4=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana4.pack(fill=tk.X)

    ventana4_1=tk.Frame(ventana4,
        background = "lightseagreen"
        )

    ventana4_2=tk.Frame(ventana4,
    background = "lightseagreen"
    )

    ventana4_2.pack(side=tk.RIGHT, padx=50)

    ventana4_1.place(relx=0.1)


    LbDNI_ENTRADA = tk.Label(ventana4_1,
        text="NÚMERO DE DNI: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VDNI=tk.IntVar()
    EnDNI_ENTRADA=tk.Entry(ventana4_1,
        textvariable = VDNI,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnDNI_ENTRADA.pack(side=tk.RIGHT,padx=80, pady=7)

    LbDNI_ENTRADA.pack(side=tk.RIGHT, padx=10, pady=4)

    BtDNI_Buscar = tk.Label(ventana4_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtDNI_Buscar.pack(side=tk.RIGHT, padx=10, pady=10)

    #################################################

    ventana5=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana5.pack(fill=tk.X)

    ventana5_1=tk.Frame(ventana5,
        background = "lightseagreen"
        )

    ventana5_2=tk.Frame(ventana5,
    background = "lightseagreen"
    )

    ventana5_2.pack(side=tk.RIGHT, padx=50)

    ventana5_1.place(relx=0.1)


    LbEDAD = tk.Label(ventana5_1,
        text="EDAD: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VEdad=tk.IntVar()
    EnEDAD=tk.Entry(ventana5_1,
        textvariable = VEdad,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnEDAD.pack(side=tk.RIGHT,padx=198, pady=7)

    LbEDAD.pack(side=tk.RIGHT, padx=10, pady=4)

    BtEDAD = tk.Label(ventana5_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtEDAD.pack(side=tk.RIGHT, padx=10, pady=10)

    #################################################

    ventana6=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana6.pack(fill=tk.X)

    ventana6_1=tk.Frame(ventana6,
        background = "lightseagreen"
        )

    ventana6_2=tk.Frame(ventana6,
    background = "lightseagreen"
    )

    ventana6_2.pack(side=tk.RIGHT, padx=50)

    ventana6_1.place(relx=0.1)

    LbF_Nacimiento = tk.Label(ventana6_1,
        text="FECHA DE NACIMIENTO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VF_Nacimiento=tk.StringVar()
    EnF_Nacimiento=tk.Entry(ventana6_1,
        textvariable = VF_Nacimiento,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnF_Nacimiento.pack(side=tk.RIGHT,padx=6, pady=7)

    LbF_Nacimiento.pack(side=tk.RIGHT, padx=10, pady=4)

    BtEDAD = tk.Label(ventana6_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtEDAD.pack(side=tk.RIGHT, padx=10, pady=10)

    ########################################

    ventana7=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana7.pack(fill=tk.X)

    ventana7_1=tk.Frame(ventana7,
        background = "lightseagreen"
        )

    ventana7_2=tk.Frame(ventana7,
    background = "lightseagreen"
    )

    ventana7_2.pack(side=tk.RIGHT, padx=50)

    ventana7_1.place(relx=0.1)


    LbN_Telefonico = tk.Label(ventana7_1,
        text="NÚMERO TELEFÓNICO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VN_Telefonico=tk.IntVar()
    EnN_Telefonico=tk.Entry(ventana7_1,
        textvariable = VN_Telefonico,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnN_Telefonico.pack(side=tk.RIGHT,padx=20, pady=7)

    LbN_Telefonico.pack(side=tk.RIGHT, padx=10, pady=4)

    BtEDAD = tk.Label(ventana7_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtEDAD.pack(side=tk.RIGHT, padx=10, pady=10)

    #######################################################

    ventana8=tk.Frame(aplicacion,
        background="lightseagreen"
        )
    ventana8.pack(fill=tk.X)

    ventana8_1=tk.Frame(ventana8,
        background = "lightseagreen"
        )

    ventana8_2=tk.Frame(ventana8,
    background = "lightseagreen"
    )

    ventana8_2.pack(side=tk.RIGHT, padx=50)

    ventana8_1.place(relx=0.1)

    LbC_Electronico = tk.Label(ventana8_1,
        text="CORREO ELECTRÓNICO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    VC_Electronico=tk.StringVar()
    EnC_Electronico=tk.Entry(ventana8_1,
        textvariable = VC_Electronico,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnC_Electronico.pack(side=tk.RIGHT,padx=4, pady=7)

    LbC_Electronico.pack(side=tk.RIGHT, padx=10, pady=4)

    BtEDAD = tk.Label(ventana8_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtEDAD.pack(side=tk.RIGHT, padx=10, pady=10)

    ######################################################

    ventana9=tk.Frame(aplicacion,
        background="lightseagreen"
        )

    ventana9.pack(fill=tk.X)

    BtNuevoPaciente = tk.Button(ventana9,
        text="NUEVO",
        font = ("Verdana", 16),
        background = "khaki1",
        relief = tk.GROOVE,
        border=5,
        width=15
    )

    def guardarPaciente():
        persona=Persona(VNombre.get(), VApellido.get(), VDNI.get(), VEdad.get(), VF_Nacimiento.get(), VN_Telefonico.get() , VC_Electronico.get())
        if idPersona==None:
            guardarPaciente(persona)


    BtGuardarPaciente = tk.Button(ventana9,
        text="GUARDAR",
        font = ("Verdana", 16),
        background = "khaki1",
        relief = tk.GROOVE,
        border=5,
        width=15,
        command=guardarPaciente
    )

    BtCancelarOp = tk.Button(ventana9,
        text="CANCELAR OPERACIÓN",
        font = ("Verdana", 16),
        background = "khaki1",
        relief = tk.GROOVE,
        border=5,
        width=20
    )

    BtGuardarPaciente.pack(side=tk.LEFT, padx=15, pady=5)

    BtNuevoPaciente.pack(side=tk.LEFT, padx=15, pady=5)

    BtCancelarOp.pack(side=tk.LEFT, padx=15, pady=5)

    ######################### FUNCIONES DE ENTRYS ##################################

##############################################################3
    #################### TABLA PACIENTES ###################

    def tablaPaciente(self,where=""):

        if len(where) >0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = mostarP()
        self.tabla = ttk.Treeview(self, column=("Nombre", "Apellidos", "DNI", "Edad", "F_Nacimiento", "N_Telefonico", "Correo"))
        self.tabla.pack()
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview) 
    #############################################################

    aplicacion.mainloop()







############ ERROR #########################

def error():

    AppError = tk.Tk()
    AppError.title("¡Vaya!")
    AppError.geometry("350x250+600+200") # resolución por defecto
    AppError.iconbitmap("error2.ico")
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
    def BucleError():
        while True:
            AppError.quit # PREGUNTAR AL PROFESOR
            interfaz()
            break

    BtError = tk.Button(AppError,
        text="Reintentar",
        font=("Arial", 10, "bold"),
        relief=tk.FLAT,
        border=2,
        background="tomato3",
        command=BucleError
        )

    BtError.place(x=135, y=145)

##################################################################

    AppError.mainloop()



