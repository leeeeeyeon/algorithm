def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    # 전부 X일 경우
    if all(all(elem == 'X' for elem in arr) for arr in maps):
        return [-1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or visited[i][j]:
                continue
            stack = [(i, j)]
            visited[i][j] = True
            days = int(maps[i][j])
            
            while stack:
                x, y = stack.pop()
                
                for k in range(4):
                    nx, ny = x + direction[k][0], y + direction[k][1]
                    
                    if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == 'X':
                        continue
                    if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                        if not visited[nx][ny]:    
                            stack.append((nx, ny))
                            visited[nx][ny] = True
                            days += int(maps[nx][ny])
                    
            answer.append(days)
            
    return sorted(answer)

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))

# 피드백
# 10번째 줄 변수와 21번째 줄 변수 이름을 i로 동일하게 하여 계속 틀렸다
# 변수 이름이 중복되지 않도록 주의하자
# 지낼 수 있는 무인도가 없을 때를 마지막에 return sorted(answer) if answer else [-1]로 더 짧게 쓸 수 있다