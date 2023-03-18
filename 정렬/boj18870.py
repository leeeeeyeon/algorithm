import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

arr = list(set(numbers))
arr.sort()

d = {}
for i in range(len(arr)):
    d[arr[i]] = i

answer = []
for elem in numbers:
    answer.append(d[elem])

print(*answer)

# 피드백
# 처음에 정렬된 리스트 arr에서 해당 원소의 인덱스를 찾기 위해 index() 함수를 사용하여
# 시간초과가 발생하였다. → O(N)

# 딕셔너리에 (원소, 인덱스)를 저장해주는 것을 통해 시간 초과 문제를 해결할 수 있었다 → O(1)