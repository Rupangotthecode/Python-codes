from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root, text="I clicked a button")
    myLabel.pack()


myButton=Button(root, text= "Click Me!", padx=10, pady=10, command=myClick)
'''attributes:
   state=DISABLED: disable the button
   padx,pady: change the  size of the button by increasing/decreqasing padding
   command: add a function to add a function to the button
   fg: change the color of the button text
   bg: change the background color
'''
myButton.pack()

root.mainloop()