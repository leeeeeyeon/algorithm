import sys

input = sys.stdin.readline

# n - 전체 날짜 수
# k - 합을 구하기 위한 연속적인 날짜의 수
n, k = map(int, input().split())

temp = list(map(int, input().split()))

# 최초
start = 0
sum = 0
result = 0
for i in range(k):
    sum += temp[i]

start += 1
result = sum

while start != n-k+1:
    sum += (temp[start+k-1]-temp[start-1])
    if sum > result:
        result = sum
    start += 1

print(result)