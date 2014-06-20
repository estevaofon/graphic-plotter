#!/usr/bin/python
from Tkinter import *
import tkMessageBox
from stringPlotting import Calculus

def changeLabel():
    eqString = equation.get()
    xAxisString = xAxisInput.get()
    equation.delete(0, END)
    equation.insert(0, eqString)
    c.plot(eqString,xAxisString)
    return

c = Calculus()
app = Tk()
app.title("Graphic Tool")
app.geometry('300x150')

labelText = StringVar()
labelText.set("Enter an Equation")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

custName= StringVar(None)
equation = Entry(app, textvariable=custName)
equation.insert(0,"f(x) = ")
equation.pack()

custName2= StringVar(None)
xAxisInput = Entry(app, textvariable=custName2)
xAxisInput.insert(0,"x from -10 to 10")
xAxisInput.pack()

button1 = Button(app, text="Plot", width=10, command = changeLabel)
button1.pack(side='bottom', padx=10, pady=10)

app.mainloop()
