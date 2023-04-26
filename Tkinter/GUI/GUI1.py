from tkinter import *

root=Tk()
root.title("MARKSHEET")


credit1=0
credit2=0
credit3=0
credit4=0
tot_cred=0
SGPAs=0

def calc_SGPA():
    global croNo1_label,croNo2_label,croNo3_label,croNo4_label,totcr_label,SGPA_label
    global credit1,credit2,credit3,credit4,tot_cred,SGPA
    if(grade1_entry.get()=='A'):
        credit1=40
    elif(grade1_entry.get()=='B'):
        credit1=36
    elif(grade1_entry.get()=='C'):
        credit1=32
    elif(grade1_entry.get()=='D'):
        credit1=28
    elif(grade1_entry.get()=='E'):
        credit1=24
    
    if(grade2_entry.get()=='A'):
        credit2=40
    elif(grade2_entry.get()=='B'):
        credit2=36
    elif(grade2_entry.get()=='C'):
        credit2=32
    elif(grade2_entry.get()=='D'):
        credit2=28
    elif(grade2_entry.get()=='E'):
        credit2=24

    if(grade3_entry.get()=='A'):
        credit3=30
    elif(grade3_entry.get()=='B'):
        credit3=27
    elif(grade3_entry.get()=='C'):
        credit3=24
    elif(grade3_entry.get()=='D'):
        credit3=21
    elif(grade3_entry.get()=='E'):
        credit3=18
    
    if(grade4_entry.get()=='A'):
        credit4=40
    elif(grade4_entry.get()=='B'):
        credit4=36
    elif(grade4_entry.get()=='C'):
        credit4=32
    elif(grade4_entry.get()=='D'):
        credit4=28
    elif(grade4_entry.get()=='E'):
        credit4=24

    croNo1_label.grid_forget()
    croNo2_label.grid_forget()
    croNo3_label.grid_forget()
    croNo4_label.grid_forget()

    croNo1_label = Label(root, text=credit1)
    croNo1_label.grid(row=3, column=9, columnspan=3)
    croNo2_label = Label(root, text=credit2)
    croNo2_label.grid(row=4, column=9, columnspan=3)
    croNo3_label = Label(root, text=credit3)
    croNo3_label.grid(row=5, column=9, columnspan=3)
    croNo4_label = Label(root, text=credit4)
    croNo4_label.grid(row=6, column=9, columnspan=3)

    tot_cred=credit1+credit2+credit3+credit4
    totcr_label.grid_forget()
    totcr_label = Label(root, text=tot_cred)
    totcr_label.grid(row=7, column=9, columnspan=3) 

    SGPAs=tot_cred/15
    SGPA_label.grid_forget()
    SGPA_label = Label(root, text=SGPAs)
    SGPA_label.grid(row=8, column=9, columnspan = 3)

name_label = Label(root, text="Name")
name_label.grid(row=0,column=0)
name_entry=Entry(root)
name_entry.grid(row=0,column=1,columnspan=3)

regNo_label = Label(root, text="Reg.No")
regNo_label.grid(row=0, column=8)
regNo_entry=Entry(root)
regNo_entry.grid(row=0,column=9,columnspan=3)

rollNo_label = Label(root, text="Roll.No")
rollNo_label.grid(row=1, column=0)
rollNo_entry=Entry(root)
rollNo_entry.grid(row=1,column=1,columnspan=3)

srlNo_label = Label(root, text="Srl.No")
srlNo_label.grid(row=2, column=0)
srlNo1_label = Label(root, text="1")
srlNo1_label.grid(row=3, column=0)
srlNo2_label = Label(root, text="2")
srlNo2_label.grid(row=4, column=0)
srlNo3_label = Label(root, text="3")
srlNo3_label.grid(row=5, column=0)
srlNo4_label = Label(root, text="4")
srlNo4_label.grid(row=6, column=0)

subNo_label = Label(root, text="Subject")
subNo_label.grid(row=2, column=1, columnspan =3)
subNo1_label = Label(root, text="CS 201")
subNo1_label.grid(row=3, column=1, columnspan =3)
subNo2_label = Label(root, text="CS 202")
subNo2_label.grid(row=4, column=1, columnspan =3)
subNo3_label = Label(root, text="MA 201")
subNo3_label.grid(row=5, column=1, columnspan =3)
subNo4_label = Label(root, text="EC 201")
subNo4_label.grid(row=6, column=1, columnspan =3)

grade_label = Label(root, text="Grade")
grade_label.grid(row=2, column=5, columnspan =3)
grade1_entry = Entry(root)
grade1_entry.grid(row=3, column=5, columnspan=3)
grade2_entry = Entry(root)
grade2_entry.grid(row=4, column=5, columnspan=3)
grade3_entry = Entry(root)
grade3_entry.grid(row=5, column=5, columnspan=3)
grade4_entry = Entry(root)
grade4_entry.grid(row=6, column=5, columnspan=3)

scrNo_label = Label(root, text="Sub Credit")
scrNo_label.grid(row=2, column=8)
scrNo1_label = Label(root, text="4")
scrNo1_label.grid(row=3, column=8)
scrNo2_label = Label(root, text="4")
scrNo2_label.grid(row=4, column=8)
scrNo3_label = Label(root, text="3")
scrNo3_label.grid(row=5, column=8)
scrNo4_label = Label(root, text="4")
scrNo4_label.grid(row=6, column=8)

croNo_label = Label(root, text="Credit Obtained")
croNo_label.grid(row=2, column=9, columnspan=3)
croNo1_label = Label(root, text=credit1)
croNo1_label.grid(row=3, column=9, columnspan=3)
croNo2_label = Label(root, text=credit2)
croNo2_label.grid(row=4, column=9, columnspan=3)
croNo3_label = Label(root, text=credit3)
croNo3_label.grid(row=5, column=9, columnspan=3)
croNo4_label = Label(root, text=credit4)
croNo4_label.grid(row=6, column=9, columnspan=3)

totcr_label = Label(root, text="Total credit")
totcr_label.grid(row=7, column=8)

SGPA_label = Label(root, text="SGPA")
SGPA_label.grid(row=8, column=8)

totcr_label = Label(root, text=tot_cred)
totcr_label.grid(row=7, column=9, columnspan=3)

SGPA_label = Label(root, text=SGPAs)
SGPA_label.grid(row=8, column=9, columnspan = 3)

submit_button = Button(root, text= "submit", bg='#03fc3d', command=calc_SGPA)
submit_button.grid(row=8, column=1, columnspan =3)

root.mainloop()