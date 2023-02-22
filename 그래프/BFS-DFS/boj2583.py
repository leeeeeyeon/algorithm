import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
areas = []

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1

dq = deque([])

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 or visited[i][j]:
            continue

        dq.append((i, j))
        visited[i][j] = True
        area = 1

        while dq:
            x, y = dq.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == 1 or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                dq.append((nx, ny))
                area += 1

        areas.append(area)

areas.sort()
print(len(areas))
print(*areas)

# 피드백
# 그래프를 탐색하는 2중 for문에서 사용하는 변수와 방향을 나타내는 for문에 i라는 변수를 중복하여 사용하여 틀렸다
# 동일한 변수명을 사용하지 않도록 주의하자
