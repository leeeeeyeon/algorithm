import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

def dijkstra(a, b):
    hq = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    visited = [[False for _ in range(n)] for _ in range(n)]

    visited[a][b] = True
    heapq.heappush(hq, (0, a, b))

    while hq:
        weight, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return weight

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if graph[nx][ny] == '1':
                heapq.heappush(hq, (weight, nx, ny))
            else:
                heapq.heappush(hq, (weight+1, nx, ny))

answer = dijkstra(0, 0)
print(answer)
