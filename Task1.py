"""
str1="hello World"
while str1:
    print("hello")
    str1=str1[1::2]
"""
"""
str1="AaBbCcDdEeFf"
var="c"
while var in str1:
    str1=str1[:-1] 
    print(var,end=" ")
"""
"""
def func(n,list1=[]):
    list1.append(list1.append(n))
    return list1
for i in range(4):
    list2=func(i)
print(list2)
"""

x=[]
if x:
    print(x,"true")
else:
    print(x,"false")    