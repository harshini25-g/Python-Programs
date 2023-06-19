#private method
class car:
    def __init__(self):                               #automativally calls
        self.__updatesoftware()                       #private method(__)denotes private
    def drive(self):
        print("Driving")
    def __updatesoftware(self):
        print("Upadting software")

blackcar=car()
blackcar.drive()          



#another example
class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="Super"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)    
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)   

c1=car()
c1.drive()
c1.setspeed(890)
#c1.__maxspeed=90                  #private variables cant be changed outside the class
#c1.drive()  

