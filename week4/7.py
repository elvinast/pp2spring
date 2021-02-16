# n = int(input())
# d = {}
# total = set()
# childs = set()
# c = {}

# for i in range(n - 1):
#     ch, par = input().split()
#     total.add(ch)
#     total.add(par)
#     childs.add(ch)
#     if d.get(par, []) != []: d[par].append(ch)
#     else: d[par] = [ch]

# def dfs(current):
#     cur = 1
#     for child in d.get(current, []):
#         cur += dfs(child)
#     c[current] = cur - 1
#     return cur

# main_parent = total.difference(childs).pop()
# dfs(main_parent)
# for item in sorted(c.items()):
#     print(item[0], item[1])

l = [j for j in input().split()]
d = {}
for i in l:
	if i in d.keys(): d[i] += 1
	else: d[i] = 1
q = list(d.items())
q.sort(key = lambda i: i[1])
for i in q: print(i.key)