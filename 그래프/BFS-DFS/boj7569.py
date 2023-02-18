import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
d = deque([])
answer = 0

# i - 층, j - 행
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1: # 시작점들을 큐에 넣는다
                d.append((i, j, k))
                visited[i][j][k] = True

while d:
    cur = d.popleft()
    x, y, z = cur[1], cur[2], cur[0]
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h or graph[nz][nx][ny] == -1 or visited[nz][nx][ny]:
            continue
        graph[nz][nx][ny] = graph[z][x][y] + 1
        visited[nz][nx][ny] = True
        d.append((nz, nx, ny))

# 0이 있는지 확인
for l in graph:
    if not all(0 not in elem for elem in l): # 안 익은 토마토가 하나라도 있다면 False
        answer = 0
        break
    else:
        for elem in l:
            mx = max(elem)
            answer = max(answer, mx)

print(answer-1)