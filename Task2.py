"""
#slice
for i in [20,10,3,4][::-1]:
    print(i)
"""

"""
#sort
for i in sorted([20,10,3,4]):
    print(i)
"""
"""
#dict
a={}
a[1]=1
a["1"]=2
a[1]=a[1]+2
a["a"]=a["1"]+3
print(a)

count=0
for i in a:
    count+=a[i]
print(count)    
"""

#list
list1=[1,2,3]
list2=[[i for i in [list1]]for i in range(4)]
print(list2)
"""

for i in range(1,20):
    if i==5:
        break
    else:
        print(i)
else:
    print("hello")        
    """