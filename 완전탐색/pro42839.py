import itertools
import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    # 문자열을 한 글자씩 잘라서 숫자로 변환
    arr = list(map(int, list(numbers)))
    
    # 순열을 구한다 (전체 경우)
    all = []
    for i in range(1, len(arr)+1):    
        all += list(itertools.permutations(arr, i))
    
    # 리스트를 숫자로 변환
    temp = []
    for elem in all:
        number = 0
        for i in range(len(elem)):
            number += 10 ** (len(elem)-1-i) * elem[i]
        temp.append(number)
    
    # 중복되는 수 제거
    temp = list(set(temp))
    
    answer = [num for num in temp if num > 1 and isPrime(num)]
    
    return len(answer)

print(solution("17"))
print(solution("011"))