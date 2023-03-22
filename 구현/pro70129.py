def solution(s):
    answer = [0, 0]
    
    one = s.count('1')
    zero = s.count('0')
    answer[0] += 1
    answer[1] += zero
    s = bin(one)
    
    while s != '0b1':
        one = s.count('1')
        zero = s.count('0') - 1
        answer[0] += 1
        answer[1] += zero
        s = bin(one)
        
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

# 다른 사람 코드
# def solution(x):
#     answer = []
    
#     cnt = 0
#     zero = 0
    
#     while True:
#         if x == '1':
#             break
#         zero = zero + x.count("0")
#         x = x.replace("0", "")
        
#         x = bin(len(x))[2:]
        
#         cnt = cnt + 1
    
#     answer = [cnt, zero]
    
#     return answer