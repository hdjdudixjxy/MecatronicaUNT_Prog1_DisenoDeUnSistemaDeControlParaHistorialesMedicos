import tkinter as tk
import datetime as dt

def buscarDNI():
    pass

def interfaz():
    
    aplicacion = tk.Tk()
    aplicacion.title("HISTORIAS CLINICAS")
    aplicacion.geometry("1366x768") # resolución por defecto
    aplicacion.iconbitmap("ICONO.ico")
    aplicacion.resizable(width=True, height=True) # ponemos que se pueda agrandar?
    aplicacion.configure(background="lightseagreen")

    #############################################################

    ventana1=tk.Frame(aplicacion,
        background="steelblue",
    )

    ventana1.pack(fill=tk.X)

    NomClinica = tk.Label(ventana1,
        text="CLÍNICA :V",
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

    EnNombre=tk.Entry(ventana2_1,
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

    EnBDNI_BUSCAR=tk.Entry(ventana2_2,
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

    EnApellido=tk.Entry(ventana3_1,
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

    EnDNI_ENTRADA=tk.Entry(ventana4_1,
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

    EnEDAD=tk.Entry(ventana5_1,
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


    LbF_NACIMIENTO = tk.Label(ventana6_1,
        text="FECHA DE NACIMIENTO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    EnF_NACIMIENTO=tk.Entry(ventana6_1,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnF_NACIMIENTO.pack(side=tk.RIGHT,padx=6, pady=7)

    LbF_NACIMIENTO.pack(side=tk.RIGHT, padx=10, pady=4)

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


    LbN_TELEFONICO = tk.Label(ventana7_1,
        text="NÚMERO TELEFÓNICO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    EnN_TELEFONICO=tk.Entry(ventana7_1,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnN_TELEFONICO.pack(side=tk.RIGHT,padx=20, pady=7)

    LbN_TELEFONICO.pack(side=tk.RIGHT, padx=10, pady=4)

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

    LbC_ELECTRONICO = tk.Label(ventana8_1,
        text="CORREO ELECTRÓNICO: ",
        font = ("Verdana", 16),
        background = "lightseagreen",
        anchor="w"
    )

    EnC_ELECTRONICO=tk.Entry(ventana8_1,
        font = ("Verdana", 16),
        background = "white",
        relief = tk.SUNKEN,
        border=5,
        width=30
    )

    EnC_ELECTRONICO.pack(side=tk.RIGHT,padx=4, pady=7)

    LbC_ELECTRONICO.pack(side=tk.RIGHT, padx=10, pady=4)

    BtEDAD = tk.Label(ventana8_2,
        text=".",
        font = ("Verdana", 16),
        background = "lightseagreen",
        foreground = "lightseagreen"
    )

    BtEDAD.pack(side=tk.RIGHT, padx=10, pady=10)

    ######################################################33
    aplicacion.mainloop()




