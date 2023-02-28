from collections import deque

def solution(maps):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    dq = deque([])
    dq.append((0, 0))
    visited[0][0] = True
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) or maps[nx][ny] == 0 or visited[nx][ny]:
                continue
                
            maps[nx][ny] += maps[x][y]
            if nx == len(maps)-1 and ny == len(maps[0])-1:
                return maps[nx][ny]
            else:
                dq.append((nx, ny))
                visited[nx][ny] = True

    return -1

# 피드백
# 처음에는 flag 변수를 사용하여 상대방 진영을 찾았는지 여부를 저장하고, 반복문을 탈출한 후 flag에 따라 최솟값 또는 -1을 answer에 저장했다
# 하지만 solution이 함수이기 때문에 바로 return을 하는 것이 더 깔끔하다