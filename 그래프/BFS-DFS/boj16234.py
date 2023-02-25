import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

graph = []
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
answer = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

def out_of_graph(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    return False

def check(): # 모든 칸의 인구수가 동일한지 확인
    p = graph[0][0]

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != p:
                return False
            
    return True

def bfs(x, y):
    dq = deque([])
    union = []

    if visited[x][y]:
        return
    
    dq.append((x, y))
    visited[x][y] = True
    union.append((x, y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]

            if out_of_graph(nx, ny) or visited[nx][ny]:
                continue
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                union.append((nx, ny))
                dq.append((nx, ny))
                visited[nx][ny] = True

    if len(union) > 1: # 원소가 0개이거나 1개인 경우 연합이 결성되지 않음을 의미한다
        unions.append(union)

while not check():
    visited = [[False for _ in range(n)] for _ in range(n)]
    unions = []
    population = []

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            bfs(i, j)

    if not unions: # 연합이 결성되지 않았을 경우 인구 이동이 멈췄음을 의미한다
        break
    
    for union in unions: # 인구 이동
        total = 0
        for x, y in union:
            total += graph[x][y]
        
        p = total // len(union)
        for x, y in union:
            graph[x][y] = p
    
    answer += 1

print(answer)

