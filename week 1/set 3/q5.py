class Student:
    name="noname"
    marks=0
    def __init__(self,name,marks): 
        self.name=name
        self.marks=marks

n=int(input("Enter number of students:"))
list=[]
for i in range(0,n):
    name=str(input("Enter name:"))
    marks=int(input("Enter marks:"))
    list.append(Student(name,marks))

list.sort(key=lambda x: x.marks, reverse=False)
print(list[n-1].name,"scored the highest with",list[n-1].marks,"marks")

