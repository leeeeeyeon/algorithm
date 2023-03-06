def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    total = sum(bridge)
    
    while bridge:
        answer += 1
        total -= bridge.pop(0)
        
        if truck_weights:
            if total + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
                total += t
            else:
                bridge.append(0)
            
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))