def fib(n):
    a = 0
    b = 1
    if(n>0):
        if n == 1:
            print(a)
        else:
            print(a,b,end=" ")
            for i in range(2,n):
               c = a + b
               a = b
               b = c
               print(c,end=" ")
    else:
        print("enter crt range")

fib(int(input("Enter range")))