s = input("ENTER A SENTENCE:")
w = s.split(" ")
nw = [i[::-1] for i in w]
ns = " ".join(nw)
print(ns)
