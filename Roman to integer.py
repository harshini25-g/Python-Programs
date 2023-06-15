x={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
t=int(input("Enter no of input: "))
for i in range(0,t,1):
  n=input("Enter input: ")
  sum=0
  for i in range(len(n)):
    if i+1!=len(n) and x[n[i]]<x[n[i+1]]:
       sum=sum-x[n[i]]
    else:
       sum=sum+x[n[i]] 
  print(sum)