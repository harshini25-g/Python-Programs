def spreadsheetencoding(n):
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=" "
    while n>0:
        n=n-1
        s=alphabets[n%26]+s
        n=n//26
    return s

spreadsheetencoding(int(input("enter input:")))    