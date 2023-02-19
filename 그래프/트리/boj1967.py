import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

def dfs(x, weight): # 시작 노드, 가중치
    for i in graph[x]:
        a, b = i # 자식 노드, 가중치
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    # 무방향 그래프이므로 양쪽 모두에 append
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

n2 = distance.index(max(distance))
distance = [-1] * (n+1)
distance[n2] = 0
dfs(n2, 0)

print(max(distance))