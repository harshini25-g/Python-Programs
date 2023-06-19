class person:
    name="harshini"
    age=20
    city="pollachi"
"""
setattr(person,'city','udumalpet')              #to change the value
x=getattr(person,'city')    
print(x)
"""
x=getattr(person,'age')                         #accessing class without using object
print(x)