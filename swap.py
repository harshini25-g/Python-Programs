"""
a=21
b=8
a,b=b,a
print("after swapping is",a,b)
"""



a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("A = {} and B = {}".format(a, b))
a = a + b
b = a - b
a = a - b
print("Now, A = {} and B = {}".format(a, b))