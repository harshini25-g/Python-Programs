#dictionaries are one of the associated datastructure in python
dict1={}                                   #1st way
dict1['sunday']=44                          #insert key and values
dict1['monday']=49
dict1['tuesday']=47
dict1['friday']=45
dict1['saturday']=43
print(dict1)

dict2={'name':'harshini','age':19,'department':'cse'}         #2nd way
print(dict2)
print(dict2.keys())                   #keys
print(dict2.values())                 #values
print(dict2['name'])

num=dict(dict2)                        #copying
print(num)

del dict1['tuesday']
print(dict1)

print('monday' in dict1)

d=dict([(1,"a"),(2,"b")])                         #3rd way using dict constructor and list of tuples
print(d)

a=[1,2,3,4]                                    #4th way using parallel list
b=["a","b","c","d"]
my_dict={}
for i in range(len(a)):
    my_dict[a[i]]=b[i]
print(my_dict)  

print(my_dict[2])
#print(my_dict['b'])       #it cant be accessed so another way is get
print(my_dict.get('b'))
my_dict[2]='cheems'         #update
print(my_dict)  

#deletion
my_dict={'name':'harshini','age':19,'department':'cse'} 
del my_dict['department']                                    #1st way
print(my_dict)

my_dict.pop('age')                                           #2nd way
print(my_dict)

my_dict.clear()                     #clear all the elements
print(my_dict)

my_dict1={'name':'harshini','age':19,'department':'cse'}      #delete whole dictionary
del my_dict1
print(my_dict1)




