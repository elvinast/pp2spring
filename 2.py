a = input().split()
# a = [int(i) for i in input().split()]
#for(int i = 0; i < n; i++)
for i in range(0, len(a), 2): #(starting point, end point, step)
    print(a[i], end = ' ')