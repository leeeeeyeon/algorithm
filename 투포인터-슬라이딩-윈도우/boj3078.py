import sys
from collections import defaultdict

input = sys.stdin.readline

# 학생 수, 등수 차이
n, k = map(int, input().split())
friends = []

for _ in range(n):
    friends.append(len(input().rstrip()))

friends += [0 for _ in range(k+1)]

left = 0
right = 0
result = 0
d = defaultdict(int)

for _ in range(k+1):
    d[friends[right]] += 1
    right += 1

if d[friends[left]] > 0:
    result += d[friends[left]]-1

while left <= n-2:
    if d[friends[left]] != 0:
        d[friends[left]] -= 1
    else:
        del d[friends[left]]

    left += 1
    d[friends[right]] += 1

    if d[friends[left]] > 0:
        result += d[friends[left]]-1
    right += 1

print(result)

# 다른 사람 코드
# n, k = map(int, input().rstrip().split())
# students = [0] * n
# data = [0] * 21
# count = 0

# for rank in range(n):
#     name = len(input().readline().rstrip())
#     students[rank] = name # 학생의 등수와 이름의 길이를 저장
#     if rank > k: # 학생의 등수가 K보다 커짐
#         data[students[rank - k - 1]] -= 1 # 자신과 상관 없는 등수의 학생을 제거
#     count += data[name] # 자신과 이름의 길이가 같은 친구를 쌍으로 추가
#     data[name] += 1 # 이름의 길이를 저장하는 리스트에 자신을 추가

# print(count)