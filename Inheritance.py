class animal:
    def eating(self):
        print("eating")

class dog(animal):
    def bark(self):                                   #def eating(self):
        print("barking")                              #print("eating")
        
d=dog()
d.eating()
d.bark()        

#another example
class animal1:
    def __init__(self,name):
        self.name=name

class dog1(animal1):
    def display(self):
        print(self.name)

d1=dog1("babydog")
d1.display()


