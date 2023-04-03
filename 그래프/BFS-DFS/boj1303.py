import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maps = []
visited = [[False for _ in range(n)] for _ in range(m)]
w, b = 0, 0

for _ in range(m):
    maps.append(input().rstrip())

def bfs(i, j, target):
    cnt = 0
    dq = deque()
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dq.append((i, j))
    visited[i][j] = True

    while dq:
        cur = dq.popleft()
        x, y = cur[0], cur[1]
        cnt += 1

        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]

            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == target:
                if not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = True

    return cnt

for i in range(m):
    for j in range(n):
        if maps[i][j] == 'W' and not visited[i][j]:
            w += bfs(i, j, 'W') ** 2
        if maps[i][j] == 'B' and not visited[i][j]:
            b += bfs(i, j, 'B') ** 2

print(w, b)

# 피드백
# 가로, 세로 반대로 하지 않도록 주의하자