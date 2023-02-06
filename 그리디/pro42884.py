def solution(routes):
    answer = 0 # 카메라 개수
    camera = -30001 # 카메라 현재 위치
    
    routes.sort(key= lambda x: x[1])
    answer += 1
    camera = routes[0][1]
    
    for i in range(1, len(routes)):
        route = routes[i]
        if route[0] <= camera:
            continue
        answer += 1
        camera = route[1]
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))