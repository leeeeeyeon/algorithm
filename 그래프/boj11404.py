import sys

input = sys.stdin.readline

INF = 1e9
n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    # 시작 도시, 도착 도시, 비용
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] < INF:
            print(graph[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print()