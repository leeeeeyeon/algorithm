import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges.sort(key = lambda x: x[2])

def find(parent, x):
    if parent[x] == x:
        return x
    parent_x = find(parent, parent[x])
    return parent_x

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

parent = []
result = 0
for i in range(n+1):
    parent.append(i)

for edge in edges:
    a, b, c = edge[0], edge[1], edge[2]

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c

print(result)
