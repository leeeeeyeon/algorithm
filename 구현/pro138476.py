from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    keys = sorted(counter.keys(), key=lambda x: -counter[x])
    
    for key in keys:
        if k - counter[key] <= 0:
            answer += 1
            break
        else:
            k -= counter[key]
            answer += 1

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))