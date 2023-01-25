import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
board = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

def bfs():
    q = deque()
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
                
    while q:
        cur = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m or temp[nx][ny] != 0:
                continue
            temp[nx][ny] = 2
            q.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    global result
    result = max(count, result)

def dfs():
    stack = []
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                stack.append((i, j))
                
    while stack:
        cur = stack.pop()
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m or temp[nx][ny] != 0:
                continue
            temp[nx][ny] = 2
            stack.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    global result
    result = max(count, result)

def make_wall(count):
    if count == 3:
        # bfs()
        dfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(count+1)
                board[i][j] = 0

result = 0
make_wall(0)
print(result)