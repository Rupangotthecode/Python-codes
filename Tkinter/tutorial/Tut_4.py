from tkinter import *

root = Tk()

e = Entry(root) #Entry is a funtion to add an input an input box

e.pack()
'''
    width: change the width of the textbox
    bg,fg: background, text color
    borderwidth: change borderwidth
    
'''

def myClick():
    howdy= "How are you doing?" + e.get()
    myLabel = Label(root, text="Hello" + e.get())
    myLabel1 = Label(root, text=howdy)
    #e.get() will get whatever is written in the textbox.

    myLabel.pack()
    myLabel1.pack()


myButton = Button(root, text="Click Me!", padx=10, pady=10, command=myClick)

myButton.pack()

root.mainloop()
