class father:
    def display(self):
        print("Base class1")

class mother:
    def display1(self):
        print("Base class2")

class child(father,mother):
    def display2(self):
        print("Derived class")    

c1=child()
c1.display()   
c1.display1() 
c1.display2()      