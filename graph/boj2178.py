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

# 피드백
# 접근 방법을 모르겠어서 책 참고 ㅠ
# 현재 위치에서 네 방향 확인(dx, dy 사용)
# 공간을 벗어나거나 벽인 경우 무시
# 해당 노드를 처음 방문하는 경우 최단 거리 기록