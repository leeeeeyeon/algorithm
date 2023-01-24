import sys
from collections import deque

input = sys.stdin.readline

# 정점, 간선, 탐색 시작 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(elem) for elem in graph]
visited = [False] * len(graph)

def dfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited[start] = True
    print(start, end = ' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    # 현재 노드 방문 처리 후 큐에서 꺼냄
    visited[start] = True

    while q:
        elem = q.popleft()
        print(elem, end = ' ')
        for i in graph[elem]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, v, visited)
print()
visited = [False] * len(graph)
bfs(graph, v, visited)