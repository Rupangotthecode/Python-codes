from tkinter import *

root = Tk() #This is the base widget of any tkinter application, it is like the base window in a program.

myLabel1 = Label(root, text="Hello World") # here we have created a label widget named myLabel and we have placed it in the root element
myLabel2 = Label(root, text="My name is Rupan")

myLabel1.grid(row=0, column=0) #grid() is a way of placing things, based on the vertical(column) and horizontal(column) tkinter axis.
myLabel2.grid(row=1, column=5)

root.mainloop() #event looping the gui
# gui using tkinter is a constantly looping program which runs in fixed intervals to check for changes.
