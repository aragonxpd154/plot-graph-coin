from __future__ import print_function #Incluir a função __future__ para ociosidade
import matplotlib
matplotlib.use("TkAgg")
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import tkinter as tk
from tkinter import ttk
import urllib
import json
import pandas as pd
import numpy as np

title=("Monitor COVID-19")
__version__ = 1.0
__date__    = "17-05-2020"
__author__  = "marcos.silvadeveloper@gmail.com"
__licence__ = "Public Domain"

LARGE_FONT=("Verdana",  12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open("data.txt","r").read()
    dataList = pullData.split('\n')
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine)>1:
            x,y=eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="./icone.ico")
        tk.Tk.wm_title(self, "Monitor COVID - 19")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight =1)

        self.frames = {}

        for F in (StartPage, PageOne, Janela1):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="""Essa é uma aplicação de Monitoramento Gráfico COVID - 19
esse aplicativo utiliza de dados externo para
monitoramento, nem a Zutup Inc, e o desenvolvedor
manipula ou mantem esses dados, é sim utiliza de
fonte externa de consulta ao Ministerio da Saude,
utilize sob sua conta e risco""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text = "Aceito",
                            command=lambda: controller.show_frame(Janela1))
        button1.pack()

        button2 = ttk.Button(self, text = "Não Aceito",
                            command=quit)
        button2.pack()
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Pagina 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1= ttk.Button(self, text="Voltar ao Inicio", command=lambda: controller.show_frame(StartPage))
        button1.pack()


class Janela1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Pagina de Gráfico", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1= ttk.Button(self, text="Voltar ao Inicio", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw() #Não usar canvas.show() para plotar desenho
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      
app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
