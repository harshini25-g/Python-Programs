"""
It is a number that is equal to the sum of its own digits raised to the power of the number of digits.

num=int(input("Enter a input:"))
sum=0
temp=num
count=len(str(num))
while temp!=0:
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10

if(sum==num):
    print("It is armstrong num")
else:
    print("Not an armstrong num")  
"""

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)        