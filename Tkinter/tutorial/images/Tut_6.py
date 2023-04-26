from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Learn to code with me')
root.iconbitmap('C:\\Users\\rupan\\OneDrive\\Documents\\Python codes\\Tkinter\\images\\icon.ico')
#  for the title image

my_img = ImageTk.PhotoImage(Image.open("icon3.png"))
my_Label = Label(image=my_img)
my_Label.pack()

#one more step needed to use pillow
#define the image(use relative path)
#put image in label
#put label(image) in root









button_quit = Button(root, text="Exit", command=root.quit)
# this causes the program to quit(prevents loop from running) 
button_quit.pack()
root.mainloop()
