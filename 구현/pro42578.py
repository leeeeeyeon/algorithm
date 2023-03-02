from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    answer = 1
    
    for a, b in clothes:
        d[b] += [a]
        
    for key in d.keys():
        # +1을 하는 이유: 해당 종류의 옷을 안 입을 경우
        answer *= len(d[key]) + 1
    
    # -1을 하는 이유: 모든 종류에서 '안 입음'을 택할 경우를 제외
    # 하루에 최소 한 개의 의상을 입기 때문
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
