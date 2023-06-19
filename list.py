list=[10,20,30,40,50.5,'hello',90]
print(list)

list[2]=22.22                    #replace
print(list)

list.insert(2,15)                #insert
print(list)


list2=[111,3,2,88,0,44,4]
list2.sort()      #sort
print(list2)

del list[4]                      #delete
print(list)

list2.append(21)                 #append
print(list2)

list2.reverse()                  #reverse
print(list2)

extra=[4,5,6,3,343]              #extend
list2.extend(extra)
print(list2)

print(len(list2))
print(max(list2))
print(min(list2))
print(list2[1:5])
print(list2.remove(21))
print(list2.pop())

result=[x**2 for x in range[1,2,3,4]]
print(result)

"""
a=list(result)
print(a)
"""


"""
len
negative index
slicing
max,min
remove
count
pop
clear
"""