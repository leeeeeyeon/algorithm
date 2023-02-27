def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = int(''.join(numbers))
    
    return str(answer)

print(solution([6,10,2]))
print(solution([3, 30, 34, 5, 9]))

# 피드백
# str로 형 변환하여 사전순으로 정렬을 한다
# 예제 2에서 3이 30보다 앞에 와야 한다. 그러므로 길이를 3배(x*3)한 문자열을 기준으로 정렬한다
# numbers의 모든 원소가 0일 때를 위해 int로 형 변환한 뒤, 다시 str로 형 변환하여 결과를 return한다