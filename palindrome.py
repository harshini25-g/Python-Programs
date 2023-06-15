"""
num = "hello"
reverse = (str(num)[::-1])
print(reverse)
"""


""""
num = 1231
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
"""


string = "123"
# this will automatically generate reverse
rev = ""
for char in string:
    rev = char + rev

print("Palindrome") if string == rev else print("Not Palindrome")

print("string: " + str(string))
print("rev: " + str(rev))