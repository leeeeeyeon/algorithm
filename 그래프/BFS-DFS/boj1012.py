import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 위치 좌표
    board = [[0 for _ in range(m)] for _ in range(n)]
    cabbage = []
    visited = []
    count = 0

    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
        cabbage.append((x, y))

    for c in cabbage: # 보드에 0인 곳도 많기 때문에 1인 곳만 탐색
        if c not in visited:
            stack = [c]
            visited.append(c)
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]
            while stack:
                cur = stack.pop()
                
                for i in range(4):
                    nx, ny = cur[0]+dx[i], cur[1]+dy[i]
                    if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny]==0 or (nx, ny) in visited:
                        continue
                    stack.append((nx, ny))
                    visited.append((nx, ny))

            count += 1

    print(count)