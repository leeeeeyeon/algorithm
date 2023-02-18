import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
d = deque([])
answer = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

if all(0 not in elem for elem in graph):
    answer = 1
else:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                d.append((i, j))
                visited[i][j] = True

    while d:
        cur = d.popleft()
        x, y = cur[0], cur[1]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == -1 or visited[nx][ny]:
                continue
            graph[nx][ny] = graph[x][y] + 1
            d.append((nx, ny))
            visited[nx][ny] = True

    for i in range(n):
        if 0 in graph[i]:
            answer = 0
            break
        mx = max(graph[i])
        answer = max(answer, mx)

print(answer-1)