import sys
from heapq import heappush, heappop

input = sys.stdin.readline

m, n = map(int, input().split()) # 가로, 세로

board = []
visited = [[False for _ in range(m)] for _ in range(n)]
hq = []
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
result = 0

for _ in range(n):
    board.append(list(map(int, list(input().rstrip()))))

heappush(hq, (0, (0, 0)))
visited[0][0] = True

while hq:
    weight, (x, y) = heappop(hq)
    if (x, y) == (n-1, m-1):
        result = weight
        break

    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
            continue

        if board[nx][ny] == 1:
            heappush(hq, (weight+1, (nx, ny)))
            visited[nx][ny] = True

        else: # board[nx][ny] == 0
            heappush(hq, (weight, (nx, ny)))
            visited[nx][ny] = True           

print(result)