import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for _ in range(m):
    x, a, b = map(int, input().split()) # 연산, a, b

    if x == 0:
        union(a, b)
    else: # x == 1
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

# 피드백
# parent 리스트를 전역 변수로 선언해야 한다