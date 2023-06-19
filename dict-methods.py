#fromkeys
list1=[1,2,3,4,5]                      #using list
print(dict.fromkeys(list1,5))          #value5 is optional

print({}.fromkeys(range(1,6),22))      #using range

#setdefault
dict={'john':22,'cheems':23,'harshini':21}
print(dict)
dict.setdefault('francis')               #add into the dict
print(dict)
dict.setdefault('goo',20)                #add into the dict with the value also
print(dict)

#concatenate 2 dictionary using dict methods
dict2={'name':'harshini','age':19,'department':'cse'} 
dict3={'john':22,'cheems':23,'harshini':21}
dict2.update(dict3)                        #update
print(dict2)
print(dict3)

#update dict using list and etc,..
ditcc={1:'a',2:'b'}
listt=[3,'c']
ditcc.update([listt])                    #list
print(ditcc)
ditcc.update(x=9,y=7,z=5)                 #assign
print(ditcc)

ditcc1={1:'harsh'}                        #overwrites
ditcc.update(ditcc1)
print(ditcc)

