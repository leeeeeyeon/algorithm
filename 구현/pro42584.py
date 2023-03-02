def solution(prices):
    answer = [0 for _ in range(len(prices))] 
    for i in range(len(prices)):
        temp = 0
        for j in range(i+1, len(prices)):
            temp += 1
            if prices[j] < prices[i]:
                break
        answer[i] = temp
    return answer

print(solution([1, 2, 3, 2, 3]))

# 다른 사람 코드
# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
 
#     for i, price in enumerate(prices):
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)

#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j

#     return answer

# 피드백
# 완전 탐색으로도 문제를 풀 수 있지만 스택이나 큐를 사용하여 효율성을 높일 수 있다