from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dq = deque()
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                    
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    dq.append((cx, cy))
    
    while dq:
        x, y = dq.popleft()
        
        if x == ix and y == iy:
            answer = visited[x][y] // 2
            break   
        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                dq.append((nx, ny))

    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],9,7,6,1))
print(solution([[1,1,5,7]],1,1,4,7))
print(solution([[2,1,7,5],[6,4,10,10]],3,1,7,10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],1,4,6,3))
