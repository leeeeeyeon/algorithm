import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = []
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    str = input()
    str = list(str)
    str.pop() # 마지막 개행 문자 pop
    maze.append(str)

for i in range(n):
    maze[i] = list(map(int, maze[i]))

q = deque()
visited[0][0] = True
q.append((0, 0))

while len(q) != 0:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if visited[nx][ny] or maze[nx][ny] != 1:
            continue
        maze[nx][ny] = maze[x][y] + 1
        q.append((nx, ny))

print(maze[n-1][m-1])