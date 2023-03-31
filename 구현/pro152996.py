from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)    
    for elem in counter.keys():
        if counter[elem] > 1:
            answer += counter[elem] * (counter[elem] - 1) // 2
    
    weights = set(weights)
    for weight in weights:
        for check in (2/3, 2/4, 3/4):
            if weight * check in weights:
                answer += counter[weight] * counter[weight * check]
            
    return answer

print(solution([100,180,360,100,270]))

# 피드백
# 1. Counter를 사용하여 동일한 원소에 대해 쌍을 센다.
# 2. set을 사용하여 중복 원소를 제거한다.
# (1에서 계산을 해주었으므로 중복 원소에 대해 고려하지 않아도 됨)
# 3. weight * check가 weights에 있는지 확인하는 과정을 통해 쌍을 센다.
# (이 때 answer += 1이 아님에 주의하자!)
