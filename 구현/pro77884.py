def count_divisor(number):
    result = 0
    for i in range(1, number+1):
        if number % i == 0:
            result += 1         
    return result

def solution(left, right):
    answer = 0
    for elem in range(left, right+1):
        cnt = count_divisor(elem)
        if cnt % 2 == 0:
            answer += elem
        else:
            answer -= elem
    return answer

# 피드백
# 약수 개수가 홀수 개인 것은 제곱수밖에 없다

# 다른 사람 풀이
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer