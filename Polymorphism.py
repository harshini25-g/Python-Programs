class dog:
    def sound(self):
        print("bark")
class cat:
    def sound(self):
        print("meow")
def makesound(animaltype):
    animaltype.sound()

d1=dog()
c1=cat()
makesound(d1)                   
makesound(c1)  