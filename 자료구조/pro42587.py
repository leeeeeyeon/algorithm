from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities = [(i, priorities[i]) for i in range(len(priorities))]
    dq = deque(priorities)
    
    while True:
        mx = max([elem[1] for elem in dq])
        index, priority = dq.popleft()
        
        if priority == mx:
            answer += 1
            if index == location:
                break
        else:
            dq.append((index, priority))

    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1], 0))
