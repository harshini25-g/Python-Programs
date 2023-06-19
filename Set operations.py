set1={1,2,3,4,'hello'}
print(6 in set1)                       #membership operator
print(4 in set1)

set1.add(6)                            #add
print(set1)

set1.remove(2)                         #remove
print(set1)

set2={1,'apple'}                        #union
print(set1|set2)                        #duplicates removed

print(set1&set2)                        #intersection
print(set1-set2)  
print(set2-set1)                        #difference

print(set1^set2)                        #symm.difference -not common values
print(len(set1))                        #size

set3=set1.copy()                        #copy
print(set3)

#set1.clear()                            #clear set
#print(set1)

