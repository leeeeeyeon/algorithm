from collections import Counter
def solution(n):
    answer = 0
    cnt = Counter(bin(n)[2:])['1']
    
    while True:
        n += 1
        if Counter(bin(n)[2:])['1'] == cnt:
            answer = n
            break
            
    return answer

print(solution(78))
print(solution(15))

# 피드백
# 2진수 변환 후 slicing 과정인 [2:]를 하지 않아도 된다
# Counter 대신 count('1')이라는 내장함수를 쓸 수 있다