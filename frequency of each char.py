str1= "harshini"
all_freq = {}
 
for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
print("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))