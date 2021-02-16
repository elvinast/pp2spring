n, m = map(int, input().split())
an = set()
am = set()
for i in range(n):
    x = int(input())
    an.add(x)
    
for i in range(m):
    x = int(input())
    am.add(x)

a = an.intersection(am)
print(len(a))
l = list(a)
l.sort()
for i in range(len(l)):
    print(l[i], end = ' ')
print()

a1 = an.difference(am)
print(len(a1))
l1 = list(a1)
l1.sort()
for i in range(len(l1)):
    print(l1[i], end = ' ')
print()

a2 = am.difference(an)
print(len(a2))
l2 = list(a2)
l2.sort()
for i in range(len(l2)):
    print(l2[i], end = ' ')
print()