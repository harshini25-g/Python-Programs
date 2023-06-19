tuple=("chemms",56,98,700,56.7)
print(tuple)
print(tuple[2])
tuple1=((56,2,3,55),(67,2,5,100))         #nested tuple
print(tuple1)
print(tuple1[1][3])                       #no operations in tuple,since it is immutable


tuple2=(1)
tuple3=(1,)                                #singleton
print(type(tuple2))
print(type(tuple3))

tuple4=tuple3+tuple1                        #concatenation
print(tuple4)

print(list(tuple4))                         #tuple into list

print(tuple3*5)