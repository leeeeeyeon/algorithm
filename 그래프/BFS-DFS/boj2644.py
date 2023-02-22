import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
a, b = map(int, input().split())

edge = int(input())
for _ in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, num):
    num += 1
    visited[x] = True

    if x == b:
        result.append(num)

    for elem in graph[x]:
        if not visited[elem]:
            dfs(elem, num)

result = []
dfs(a, 0)
if result:
    print(result[0]-1)
else: # 하나의 트리 안에 있지 않다면 result가 empty
    print(-1)