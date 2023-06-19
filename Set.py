#set 
fruits={'apple','orange','mango'}
print(fruits)
fruits.add('grapes')               #mutuable
print(fruits)

sett=frozenset(['a','b','c'])             #immutuable set using frozenset keyword
print(sett)
#set.add('c')                              #frozen cant be changes error

set2={}                   #empty dict
print(type(set2))
set1=set()
print(type(set1))

#copy set
num={1,2,3,4}
print(num)
num1=set(num)                       #to copy
print(num1)