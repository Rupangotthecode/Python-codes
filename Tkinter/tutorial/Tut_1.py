from tkinter import *

root = Tk() #This is the base widget of any tkinter application, it is like the base window in a program.

myLabel1 = Label(root, text="Hello World") # here we have created a label widget named myLabel and we have placed it in the root element

myLabel1.pack() #pack() is an unsophisticated way of just shoving things, without much specification abt the properties of the element.

root.mainloop() #event looping the gui
# gui using tkinter is a constantly looping program which runs in fixed intervals to check for changes.
