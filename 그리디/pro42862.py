from collections import defaultdict

def solution(n, lost, reserve):
    d = defaultdict(int)
    
    lost.sort()
    reserve.sort()
    
    # 모든 학생이 체육복을 가져옴
    for i in range(n+2):
        # index out of range 방지
        if i==0 or i==n+1:
            d[i] = 0
        else:
            d[i] += 1
    
    # 체육복을 도난 당한 학생
    for elem in lost:
        d[elem] -= 1
    
    # 여벌 체육복이 있는 학생
    for elem in reserve:
        d[elem] += 1
        
    for elem in lost:
        # 도난 당했지만 여벌 체육복이 있는 학생은 체육복을 빌리지 X
        if d[elem] == 0:
            # 앞 번호 친구부터 check    
            if d[elem-1] > 1:
                d[elem-1] -= 1
                d[elem] += 1
            # 뒷 번호 친구를 다음으로 check
            elif d[elem+1] > 1:
                d[elem+1] -= 1
                d[elem] += 1
    
    attempt = [i for i in list(d.keys()) if d[i] > 0]

    return len(attempt)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

# 피드백
# 13번, 14번 테스트 케이스에서 계속 틀렸다
# 반례: 5, [4, 2], [3, 5] (참고: https://school.programmers.co.kr/questions/35069)
# lost와 reserve를 정렬해주어 해결할 수 있었다.

# 다른 사람 코드
# def solution(n, lost, reserve):
#     set_reserve = set(reserve) - set(lost)
#     set_lost = set(lost) - set(reserve)

#     for i in set_reserve:
#         if i-1 in set_lost:
#             set_lost.remove(i-1)
#         elif i+1 in set_lost:
#             set_lost.remove(i+1)
#     return n-len(set_lost)