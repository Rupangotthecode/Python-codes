from tkinter import *

root = Tk()
root.title("registration form")
root.geometry('500x300')
root.configure(bg='#03fc3d')

Form_label = Label(root, text="Form",bg='#03fc3d')
Form_label.grid(row=0, column=5)

Name_label = Label(root, text="Name",bg='#03fc3d')
Name_label.grid(row=1, column=0)
name=Entry(root,width=50)
name.grid(row=1, column=1,columnspan=9)

course_label = Label(root, text="Course",bg='#03fc3d')
course_label.grid(row=2, column=0)
course=Entry(root,width=50)
course.grid(row=2, column=1,columnspan=9)

sem_label = Label(root, text="Semester",bg='#03fc3d')
sem_label.grid(row=3, column=0)
sem=Entry(root,width=50)
sem.grid(row=3, column=1,columnspan=9)

Fno_label=Label(root, text="Form No.",bg='#03fc3d')
Fno_label.grid(row=4, column=0)
Fno=Entry(root,width=50)
Fno.grid(row=4, column=1,columnspan=9)

Cno_label = Label(root, text="Contact no.",bg='#03fc3d')
Cno_label.grid(row=5, column=0)
Cno=Entry(root,width=50)
Cno.grid(row=5, column=1,columnspan=9)

email_label = Label(root, text="Email id",bg='#03fc3d')
email_label.grid(row=6, column=0)
email=Entry(root,width=50)
email.grid(row=6, column=1,columnspan=9)

address_label = Label(root, text="Address",bg='#03fc3d')
address_label.grid(row=7, column=0)
address=Entry(root,width=50)
address.grid(row=7, column=1,columnspan=9)

submit_button=Button(root, text="Submit",bg='red')
submit_button.grid(row=8, column=5)

root.mainloop()