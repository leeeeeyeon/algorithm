import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
alphabet = set()
ans = 0

# 입력
for _ in range(r):
    graph.append(list(input().rstrip()))

def dfs(x, y, count):
    global ans
    ans = max(ans, count)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in alphabet:
            alphabet.add(graph[nx][ny])
            dfs(nx, ny, count+1)
            alphabet.remove(graph[nx][ny])

alphabet.add(graph[0][0])
dfs(0, 0, 1)

print(ans)