#vehicle data
class Vehicle:
    name=""
    number=""
    def inputter(self):
        self.name=input("Enter name of vehicle:")
        self.number=input("Enter car number:")
    def display(self):
        print("Name of vehicle:",self.name)
        print("Vehicle number:",self.number)
class Bus(Vehicle):
    passengers=0
    def inputter(self):
        super().inputter()
        self.passengers=int(input("Enter the number of passengers:"))
    def display(self):
        print("Name of Bus:",self.name)
        print("Bus number:",self.number)
        print("Passengers count=",self.passengers)
v1=Vehicle()
v1.inputter()
v1.display()
b1=Bus()
b1.inputter()
b1.display()