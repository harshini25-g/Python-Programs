class person:
    def display(self):
        print("base class")

class person1(person):
    def display1(self):
        print("derived class 1")  


class person2(person1):
    def display2(self):
        print("derived class 2")

p1=person2()
p1.display()  
p1.display1() 
p1.display2()                       