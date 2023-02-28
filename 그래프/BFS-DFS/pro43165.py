def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(index, result):
        if index == n: 
            if result == target:
                nonlocal answer
                answer += 1
            return
        dfs(index+1, result+numbers[index])
        dfs(index+1, result-numbers[index])
        
    dfs(0, 0)
    
    return answer

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))