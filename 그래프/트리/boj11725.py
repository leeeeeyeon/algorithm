import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(x):
    visited[x] = True

    for elem in graph[x]:
        if not visited[elem]:
            dfs(elem)
            parents[elem] = x

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

for i in range(2, n+1):
    print(parents[i])
