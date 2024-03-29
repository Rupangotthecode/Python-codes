from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('C:\\Users\\rupan\\OneDrive\\Documents\\Python codes\\Tkinter\\images\\icon.ico')

my_img1 = ImageTk.PhotoImage(Image.open("icon6.png"))
my_img2 = ImageTk.PhotoImage(Image.open('icon2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('icon3.png'))
my_img4 = ImageTk.PhotoImage(Image.open('icon4.png'))
my_img5 = ImageTk.PhotoImage(Image.open('icon5.png'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan= 3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_back = Button(root, text="<<", command= lambda: back(image_number-1))
    button_forward = Button(root, text=">>", command= lambda: forward(image_number+1))
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

def back():
    global my_label
    global button_forward
    global button_back

button_back = Button(root, text="<<", command= back)
button_exit = Button(root, text="Exit Program", command= root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()