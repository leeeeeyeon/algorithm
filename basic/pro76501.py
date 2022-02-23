# 내 코드
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
    for elem in absolutes:
        answer += elem
    return answer

print(solution([1,2,3], [False,False,True]))

# 다른 사람 코드
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 피드백
# zip: 동일한 개수로 이루어진 자료형을 튜플의 형태로 묶어 주는 역할을 하는 함수
# if ~~~ == True 대신 if ~~~ / if ~~~ == False 대신 if not ~~~