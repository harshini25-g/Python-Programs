class father:
    def display(self):
        print("welcome")

class mother(father):
    def display(self):
        print("Method overriding")

m1=mother()
m1.display()               