def solution(park, routes):
    answer = []
    direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
        
    # 1. 시작 지점을 찾는다
    location = [0, 0]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                location = [i, j]
    
    # 2. routes에 주어진 명령에 따라 움직인다
    for route in routes:
        ox, oy = location[0], location[1]
        op, n = route.split()
        n = int(n)
        
        for _ in range(n):
            x, y = location[0], location[1]
            nx, ny = x + direction[op][0], y + direction[op][1]
            
            # 범위 이탈 or 장애물을 만났을 시 해당 명렁 pass
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]) or park[nx][ny] == 'X':
                location = [ox, oy]
                break
            else:
                location = [nx, ny]
        
    return location

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]	))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))