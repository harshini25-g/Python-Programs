#non-duplicate values selection sort
list=[99,2,56,45,71,8]
print("unsorted list",list)

for i in range(len(list)):
    min_value=min(list[i:])                               #max-descending order
    min_index=list.index(min_value)
    list[i],list[min_index]=list[min_index],list[i]
print("sorted list",list)



#duplicate values selection sort
list=[99,2,56,2,45,71,8]
print("unsorted list",list)

for i in range(len(list)):
    min_value=min(list[i:])                               #max-descending order
    min_index=list.index(min_value,i)                     #duplicate values
    if list[i]!=list[min_index]:                 
        list[i],list[min_index]=list[min_index],list[i]
print("sorted list",list)