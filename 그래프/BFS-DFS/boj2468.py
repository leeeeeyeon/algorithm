import sys

input = sys.stdin.readline

n = int(input())

graph = []
mx = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    mx = max(mx, max(arr))
    graph.append(arr)

answer = 0
for height in range(0, mx):
    temp = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height or visited[i][j]:
                continue
            stack = []
            stack.append((i, j))

            while stack:
                cur = stack.pop()
                dx = [0, 1, 0, -1]
                dy = [-1, 0, 1, 0]
                for k in range(4):
                    nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] <= height or visited[nx][ny]:
                        continue
                    stack.append((nx, ny))
                    visited[nx][ny] = True
            temp += 1
    answer = max(temp, answer)

print(answer)

# 피드백
# 아무 지역도 물에 잠기지 않을 수도 있다. = 비의 양이 0일 수도 있다는 뜻!
# height의 반복문 범위를 0부터로 해야 한다!