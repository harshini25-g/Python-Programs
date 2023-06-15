l=[1,2,3,8,9,6,9,7,5,4,2,8,0]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=" ")