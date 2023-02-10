import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])

edges.sort(key = lambda x: (x[0], x[1]))

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = parent[root_a]
    else:
        parent[root_a] = parent[root_b]

parent = []
for i in range(n+1):
    parent.append(i)

for _ in range(2):
    for edge in edges:
        a, b = edge[0], edge[1]

        if find(parent, a) != find(parent, b):
            union(parent, a, b)

print(len(set(parent))-1)