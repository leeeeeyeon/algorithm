import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
stack = deque()

for i in range(n):
    graph.append(list(str(input().rstrip())))

def dfs(x, y):
    stack.append((x, y))

    # 스택에 아무 노드가 없을 때까지
    while stack:
        # 1. 스택 가장 위 노드를 꺼낸다.
        v = stack.pop()
        x = v[0]
        y = v[1]
        target = graph[x][y] # 현재 칸의 색깔

        # 방문하지 않았다면
        if not visited[x][y]:
            # 방문 표시
            visited[x][y] = True

            for i in range(4):
                # x, y 값 기준점으로 초기화
                x = v[0]
                y = v[1]

                # 위, 아래, 왼쪽, 오른쪽 순
                nx = [-1, 1, 0, 0]
                ny = [0, 0, -1, 1]

                x += nx[i]
                y += ny[i]

                # 인덱스를 벗어날 경우 skip
                if x <= -1 or x >= n or y <= -1 or y >= n:
                    continue

                # 인접한 노드이면서 스택에 없는 노드이면
                # 스택에 넣지만 방문 체크는 안 함
                if graph[x][y] == target and not visited[x][y]:
                    stack.append((x, y))

    return 1
                    
result = [0, 0]
# 적록색약이 아닐 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result[0] += dfs(i, j)

# 적록색약일 경우
# 방문 배열 초기화
visited = [[False] * n for _ in range(n)]

# G를 R로 교체
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
                graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result[1] += dfs(i, j)
       
print(result[0], result[1])
