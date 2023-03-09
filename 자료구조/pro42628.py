from heapq import heapify, heappush, heappop

def solution(operations):
    answer = []
    hq = []
    
    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)

        if alphabet == 'I':
            heappush(hq, number)    
        else: # alphabet == 'D'
            if hq: # 빈 큐에서 데이터를 삭제하라는 연산이 주어졌을 시 무시
                if number == -1:
                    heappop(hq) # 최솟값을 삭제
                else:
                    hq.pop() # 최댓값을 삭제
                    
    # 모든 연산을 처리한 후
    hq.sort()
    if hq: # 큐가 비어있지 않음
        answer = [hq[-1], hq[0]]
    else: # 큐가 비어있음
        answer = [0, 0]
        
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 4", "I -1", "I 6", "I 3"]))

# 피드백
# 힙은 이진 트리고, 우리가 사용하는 리스트는 트리를 1차원 형태로 표현한 것이다.
# heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
# 힙은 정렬된 리스트와 다르다는 것을 주의하자