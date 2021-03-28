from sense_emu import SenseHat
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk
import time
import matplotlib.pyplot as plt

class Aplicacion:
    def __init__(self):
        self.funcionamiento = True
        self.periodo = 1000

        #while (self.funcionamiento == True):
        #    print(self.temp)

        self.ventana=tk.Tk()
        self.ventana.title('Práctica GUI SenseHAT')
        self.label1=tk.Label(self.ventana, text="Opciones")
        self.label1.grid(column=0, row=0)

        self.cuaderno1=ttk.Notebook(self.ventana)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Monitorización")

        self.labelframe1=ttk.LabelFrame(self.ventana, text="Control")
        self.labelframe1.grid(column=0, row=2, padx=5, pady=10)
        self.control()

        self.labelframe2=ttk.LabelFrame(self.ventana, text="Medidas")
        self.labelframe2.grid(column=0, row=4, padx=5, pady=10)
        self.medidas()

        self.scroll1 = tk.Scrollbar(self.ventana, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self.ventana, yscrollcommand=self.scroll1.set)
        self.tree.grid()
        
        self.scroll1.configure(command=self.tree.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')
        
        self.tree['columns'] = ('valor', 'fecha/hora', 'tipo')

        self.tree.heading('#0', text='#NUM')
        self.tree.heading('valor', text='Valor')
        self.tree.heading('fecha/hora', text='Fecha/Hora')
        self.tree.heading('tipo', text='Tipo')

        
        

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Gráfica")
        
        self.cuaderno1.grid(column=0, row=1)

        self.ventana.after(self.periodo, self.obtener_medida)

        self.ventana.mainloop()

    def control(self):
        self.boton = tk.Button(self.labelframe1, text="Parar", command=self.stop)
        self.color_boton()
        self.boton.grid(column=5, row=2, padx=4, pady=4)
        self.label2 = tk.Label(self.labelframe1, text="Periodo")
        self.label2.grid(column=4, row=3, padx=4, pady=4)
        self.label3 = tk.Label(self.labelframe1, text=self.periodo)
        self.label3.grid(column=6, row=3, padx=4, pady=4)

    def color_boton(self):
        if self.funcionamiento == True:
            self.boton.configure(background="green")
        else:
            self.boton.configure(background="red")
    
    def stop(self):
        if self.funcionamiento == True:
            self.funcionamiento = False
        else:
            self.funcionamiento = True
        
        self.color_boton()
        
    def medidas(self):
        self.sense = SenseHat()

        self.temp = self.sense.temperature
        self.pre = self.sense.pressure
        self.hum = self.sense.humidity
        
        self.seleccion = tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(column=4, row=6)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Presión", variable=self.seleccion, value=2)
        self.radio2.grid(column=5, row=6)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion, value=3)
        self.radio2.grid(column=6, row=6)
        self.texto = str('')
        if self.seleccion == 1:
            self.texto = str(self.temp)
        elif self.seleccion == 2:
            self.texto = str(self.pre)
        elif self.seleccion == 3:
            self.texto = str(self.hum)
        self.label4=tk.Label(self.ventana, text=self.texto)
        self.label4.grid(column=5, row=5, padx=4, pady=4)

    def obtener_medida(self):
        if self.seleccion == 1:
            self.texto = str(self.temp)
        elif self.seleccion == 2:
            self.texto = str(self.pre)
        elif self.seleccion == 3:
            self.texto = str(self.hum)

    


aplicacion1=Aplicacion()




