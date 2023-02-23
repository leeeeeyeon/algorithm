import sys

input = sys.stdin.readline

def solution(arr):
    answer = []

    answer.append(arr[0])
    for elem in arr:
        if elem == answer[-1]:
            continue
        else:
            answer.append(elem)
            
    return answer

l = list(map(int, input().split()))

print(solution(l))