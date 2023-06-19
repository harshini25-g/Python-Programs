"""
n=int(input("Enter an num:"))
rev=0
while n!=0:
    rev=(rev*10)+n%10
    n=n//10
print("Reversed num is:",rev)   
"""

int1=int(input("Enter a num:"))
str1=int(str(int1)[::-1])
print(str1)
