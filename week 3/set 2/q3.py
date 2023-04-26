class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area = ",self.length*self.breadth)
    def perimeter(self):
        print("Perimeter = ",2*(self.length+self.breadth))
l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
r1=Rectangle(l,b)
r1.area()
r1.perimeter()