class Mammal:
    def __init__(self,name):
        self.name=name
        print(self.name,"is a mammal.")
class Elephant(Mammal):
    def __init__(self, name, legs):
        super().__init__(name)
        print(self.name,"has",legs,"legs and can walk")
class Whale(Mammal):
    def __init__(self, name, canSwim=False):
        super().__init__(name)
        if(canSwim):
            print("It can swim")
class Reptile(Elephant,Whale):
    def __init__(self, name, legs,canSwim):
        super().__init__(name, legs)
        super().__init__(name, canSwim)
Reptile("Roxy Croc",4,True)