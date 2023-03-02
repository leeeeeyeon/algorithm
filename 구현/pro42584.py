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