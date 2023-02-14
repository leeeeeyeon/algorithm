import sys

input = sys.stdin.readline

while True:
    w, h = map(int, input().split()) # 지도의 너비와 높이
    
    if w == 0 and h == 0: # 입력의 마지막 줄에는 0이 두 개 주어짐
        break

    graph = [[0 for _ in range(w)] for _ in range(h)] # 지도
    visited = [[False for _ in range(w)] for _ in range(h)] # 방문 여부
    stack = [] # 스택

    for i in range(h): # 지도 입력 받음
        graph[i] = list(map(int, input().split()))

    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0 or visited[i][j]:
                continue
            else:
                stack.append((i, j))
                while stack:
                    dx = [0, 1, 1, 1, 0, -1, -1, -1]
                    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

                    cur = stack.pop()
                    for k in range(8):
                        nx, ny = cur[0]+dx[k], cur[1]+dy[k]

                        if nx < 0 or nx >= h or ny < 0 or ny >= w or graph[nx][ny] == 0 or visited[nx][ny]:
                            continue
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                answer += 1

    print(answer)
