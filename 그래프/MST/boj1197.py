import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges.sort(key=lambda x: x[2])

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a

parent = []
result = 0
for i in range(v+1):
    parent.append(i)

for edge in edges:
    a, b, c = edge[0], edge[1], edge[2]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c

print(result)