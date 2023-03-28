from collections import deque

def bfs(start, end, maps):
    dq = deque()
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    dq.append((start[0], start[1], 0))
    
    while dq:
        x, y, dist = dq.popleft()
        
        if (x, y) == end:
            return dist
        
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]

            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) or maps[nx][ny] == 'X' or visited[nx][ny]:
                continue
            dq.append((nx, ny, dist+1))
            visited[nx][ny] = True
                
    return 0

def solution(maps):
    # 시작 지점, 출구, 레버의 위치를 저장
    points = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                points['S'] = (i, j)
            elif maps[i][j] == 'E':
                points['E'] = (i, j)
            elif maps[i][j] == 'L':
                points['L'] = (i, j)
    
    sl = bfs(points['S'], points['L'], maps)
    if sl == 0:
        return -1
    le = bfs(points['L'], points['E'], maps)
    if le == 0:
        return -1

    return sl + le

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))

# 피드백
# visited 배열 필요!
# points 저장할 때 반복문 인덱스 잘못했음 ㅋㅋ ㅠㅠ
