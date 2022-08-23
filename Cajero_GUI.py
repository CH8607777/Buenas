
from tkinter import *
import tkinter as tk
from tkinter import ttk

class VentanaSecundaria1(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana Ingresar")
        self.geometry("400x200")
        self.resizable(0, 0)
        self.boton_cuant0 = ttk.Button(
        self,
            text="¿Cuánto dinero desea ingresar?"
        )
        self.boton_cuant0.pack()
        self.boton_2000 = ttk.Button(
        self,
            text="2000",
            command=self.ingresar3
        )
        self.boton_2000.pack()
        self.boton_3000 = ttk.Button(
        self,
            text="3000", 
            command=self.ingresar3
        )
        self.boton_3000.pack()
        self.focus()
        self.grab_set()
        self.boton_4000 = ttk.Button(
        self,
            text="4000", 
            command=self.ingresar3
        )        
        self.boton_4000.pack()
        self.focus()
        self.grab_set()
        self.boton_otro = ttk.Button(
        self,
            text="Otro", 
            command=self.VentanaOtro
        )
        self.boton_otro.pack()
        self.focus()
        self.grab_set()
        self.boton_cerrar = ttk.Button(
        self,
            text="cerrar", 
            command=self.destroy
        )        
        self.boton_cerrar.pack()
        self.focus()
        self.grab_set()
    class VentanaOtro(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            self.config(width=300, height=90)
            self.resizable(0, 0)
            self.title("Otro")
            self.caja_nombre = ttk.Entry(self)
            self.caja_nombre.place(x=20, y=20, width=260)
            self.boton_listo = ttk.Button(
            self,
                text="Ingresar",
                command=self.ingresar3
            )
            self.boton_listo.place(x=20, y=50, width=260)
            self.focus()
            self.grab_set()
        def ingresar3(self):
            self.boton_1 = ttk.Button(
            self,
                text="Dinero ingresado correctamente",
                command=self.destroy
            )
            self.boton_1.pack()
            self.focus()
            self.grab_set()
    def ingresar3(self):
        self.boton_1 = ttk.Button(
        self,
            text="Dinero ingresado correctamente",
            command=self.destroy
        )
        self.boton_1.pack()
        self.focus()
        self.grab_set()
class VentanaSecundaria2(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana Retirar")
        self.geometry("400x200")
        self.resizable(0, 0)
        self.boton_cuanto = ttk.Button(
        self,
            text="¿Cuánto dinero desea retirar?"
        )
        self.boton_cuanto.pack()
        self.focus()
        self.grab_set()

        self.boton_1000 = ttk.Button(
        self,
            text="1000",
            command=self.retirar
        )
        self.boton_1000.pack()
        self.focus()
        self.grab_set()

        self.boton_5000 = ttk.Button(
        self,
            text="5000",
            command=self.retirar
        )
        self.boton_5000.pack()
        self.focus()
        self.boton_otro2 = ttk.Button(
        self,
            text="Otro", 
            command=self.VentanaOtro2
        ) 
        self.boton_otro2.pack()
        self.grab_set()
        self.boton_cerrar = ttk.Button(
        self,
            text="cerrar", 
            command=self.destroy
        )        
        self.boton_cerrar.pack()
        self.focus()
        self.grab_set()
    class VentanaOtro2(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            self.config(width=300, height=90)
            self.resizable(0, 0)
            self.title("Ingresa una cantidad")
            self.caja_nombre = ttk.Entry(self)
            self.caja_nombre.place(x=20, y=20, width=260)
            self.boton_listo = ttk.Button(
            self,
                text="Retirar",
                command=self.retirar3
            )
            self.boton_listo.place(x=20, y=50, width=260)
            self.focus()
            self.grab_set()
        def retirar3(self):
            self.boton_1 = ttk.Button(
            self,
                text="Dinero retiardo correctamente",
                command=self.destroy
            )
            self.boton_1.pack()
            self.focus()
            self.grab_set()
    def retirar(self):
        self.boton_2 = ttk.Button(
        self,
            text="Gracias por usar nuestro cajero",
            command=self.destroy
        )
        self.boton_2.pack()
        self.focus()
        self.grab_set()
class VentanaSecundaria3(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        saldo = 10000
        super().__init__(*args, **kwargs)
        self.title("Ventana Mostrar")
        self.resizable(0, 0)
        self.geometry("260x30")
        self.boton_saldo = ttk.Button(
        self,
            text=(f"Su dinero es de {saldo} Dolares"),
            command=self.destroy        
        )
        self.boton_saldo.pack()
        self.focus()
        self.grab_set()
class VentanaEjemplo(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CAJERO")
        self.geometry("400x200")
        self.resizable(0, 0)
        self.etiqueta = Label(text=">MENU<")
        self.etiqueta.pack()
        self.boton_ingresar = ttk.Button(
        self,
            text="Ingresar dinero",
            command=self.abrir_ventana_secundaria1
        )
        self.boton_ingresar.pack()
        self.boton_retirar = ttk.Button(
            self,
            text="Retirar dinero",
            command=self.abrir_ventana_secundaria2
        )
        self.boton_retirar.pack()
        self.boton_mostrar = ttk.Button(
            self,
            text="Mostrar dinero en la cuenta",
            command=self.abrir_ventana_secundaria3
        )
        self.boton_mostrar.pack()
        self.boton_cerrar = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
            )
        self.boton_cerrar.pack()
    def abrir_ventana_secundaria1(self):
        self.ventana_secundaria1 = VentanaSecundaria1()
    def abrir_ventana_secundaria2(self):
        self.ventana_secundaria2 = VentanaSecundaria2()
    def abrir_ventana_secundaria3(self):
        self.ventana_secundaria3 = VentanaSecundaria3()
MiVentana = VentanaEjemplo()
#MiVentana.iconbitmap('ATM.ico')
#img = PhotoImage(file="Cajero.ico")
#widget = Label(VentanaEjemplo, image=img).pack()
MiVentana.mainloop()