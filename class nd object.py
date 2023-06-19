class person:
    def  display(self):                        #method is display
        print("hello")

#main
p=person()
p.display()                                   #acccessing method using object

#initialize object
#init method
class stud:
    def __init__(self,name):
      self.name=name                      #when object is called,this method is called automatically and it is an instance var
    def disp(self):
        print("hello",self.name)

#orld=stud("harshini")           
#world.disp()       

stud("harshini").disp()    
