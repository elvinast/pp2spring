d = {}
sInput = []
f = []
import sys
sInput = (str(sys.stdin.read()).split()) #чтобы считывать все
for i in sInput:
    if i in d.keys():
        d[i] += 1
    else: d[i] = 1

def checking(x):
    return(-x[0], x[1])  

d[i].

for key, value in d.items():
	f.append((value, key))
f.sort(key=checking)
for i in f:
    print(i[1])