
from dronLink.Dron import Dron
import time
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
import asyncio


dron = Dron()
dron.connect('tcp:127.0.0.1:5763', 115200)
blockingFlag = False # Una flag por si quieres que los comandos sean asincronos

# region callbacks

# Referencia https://ccia.ugr.es/mgsilvente/tkinterbook/tkinter-entry-dialogs.htm

def changeAlt():
    alt = tkinter.simpledialog.askinteger('Change Altitude', "Set the new altitude:")
    dron.change_altitude(alt)

def goto():
    coordinates = tkinter.simpledialog.askstring('Go to ...', "Set the destination coordinates in the format \"lat;lon;alt\":")
    component = coordinates.split(';')
    dron.goto(float(component[0]),float(component[1]),float(component[2]), blocking=blockingFlag)

# endregion callbacks


# region App

# Referencia https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/
class App(ttk.Frame):
    def __init__(self, window):
        super().__init__(window)
        window.title("Dron controller")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.pack(fill=tk.BOTH, expand=True, side="right")
        """
        self.row1 = tk.Frame(self)
        self.row1.pack(side= "top", expand=True, fill=tk.BOTH)
        self.row1.columnconfigure(0, weight=1)
        self.row1.columnconfigure(1, weight=1)
        self.row1.columnconfigure(2, weight=1) """

        self.armBtn = tk.Button(self, text="Arm", command=lambda: dron.arm(blocking=blockingFlag) , bg="cyan")
        """ self.armBtn.pack(side=tk.LEFT, expand=True, fill= tk.BOTH) """
        self.armBtn.grid(row=0,column=0, sticky="nsew")

        self.takeOffBtn = tk.Button(self, text="Take off", command=lambda: dron.takeOff(10, blocking=blockingFlag), bg="cyan")
        """ self.takeOffBtn.pack(side=tk.LEFT, expand=True, fill= tk.BOTH) """
        self.takeOffBtn.grid(row=0,column=1, sticky="nsew")

        self.landBtn = tk.Button(self, text="Land",command=lambda: dron.land(blocking=blockingFlag), bg="cyan")
        """ self.landBtn.pack(side=tk.LEFT, expand=True, fill= tk.BOTH) """
        self.landBtn.grid(row=0,column=2, sticky="nsew")

        """ self.row2 = tk.Frame(self)
        self.row2.pack(side= "top", expand=True, fill=tk.BOTH)
        self.row2.columnconfigure(0, weight=1)
        self.row2.columnconfigure(1, weight=1)
        self.row2.columnconfigure(2, weight=1) """

        self.RTLBtn = tk.Button(self, text="RTL", command=lambda: dron.RTL(blocking=blockingFlag) , bg="cyan")
        """ self.RTLBtn.pack(side=tk.LEFT, expand=True, fill= tk.BOTH) """
        self.RTLBtn.grid(row=1,column=0, sticky="nsew")

        self.gotoBtn = tk.Button(self, text="Go to ...", command=goto, bg="cyan")
        self.gotoBtn.grid(row=1,column=1, sticky="nsew")

        self.changeAltBtn = tk.Button(self, text="Change alt" ,command=changeAlt, bg="cyan")
        self.changeAltBtn.grid(row=1,column=2, sticky="nsew")

        self.NEBtn = tk.Button(self, text="NE", command=lambda: dron.go('NorthEast'), bg="yellow")
        self.NEBtn.grid(row=2,column=0, sticky="nsew")

        self.upBtn = tk.Button(self, text="North", command=lambda: dron.go('North'), bg="yellow")
        """ self.upBtn.pack(side=tk.LEFT, expand=True, fill= tk.BOTH) """
        self.upBtn.grid(row=2,column=1, sticky="nsew")

        self.NWBtn = tk.Button(self, text="NW", command=lambda: dron.go('NorthWest'), bg="yellow")
        self.NWBtn.grid(row=2,column=2, sticky="nsew")

        self.eastBtn = tk.Button(self, text="East", command=lambda: dron.go('East'), bg="yellow")
        self.eastBtn.grid(row=3,column=0, sticky="nsew")

        self.stopBtn = tk.Button(self, text="Stop", command=lambda: dron.go('Stop'), bg="yellow")
        self.stopBtn.grid(row=3,column=1, sticky="nsew")

        self.westBtn = tk.Button(self, text="West", command=lambda: dron.go('West'), bg="yellow")
        self.westBtn.grid(row=3,column=2, sticky="nsew")

        self.SEBtn = tk.Button(self, text="SE", command=lambda: dron.go('SouthEast'), bg="yellow")
        self.SEBtn.grid(row=4,column=0, sticky="nsew")

        self.southBtn = tk.Button(self, text="South", command=lambda: dron.go('South'), bg="yellow")
        self.southBtn.grid(row=4,column=1, sticky="nsew")

        self.SWBtn = tk.Button(self, text="SW", command=lambda: dron.go('SouthWest'), bg="yellow")
        self.SWBtn.grid(row=4,column=2, sticky="nsew")
        

# endregion App

window = tk.Tk()
window.title("Dron Controller")
window.geometry('400x300')

app = App(window)

app.mainloop()
dron.RTL(blocking=blockingFlag)
dron.disconnect()