def decode(col):
    c=ord('A')
    ret= 0
    for i in col:
        i=ord(i)
        ret=(ret*26)+i-c+1
    return ret
col=input("Enter input:")
col=col.upper()
print(decode(col))


