class student:
    clg='abc'          #class variable
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)   
        print("College:",student.clg)

stu1=student("harshini","abc111")
stu1.display()           

stu2=student("harsh","abc121")
stu2.display() 

#static method
class a:
    @staticmethod
    def display1():
        print("hello")

a1=a()
a1.display1()        