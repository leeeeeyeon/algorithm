import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
remainder = [0 for _ in range(m)]
remainder[0] = 1

total = 0
for i in range(n):
    total += arr[i]

    remainder[total % m] += 1

count = 0
for elem in remainder:
    count += elem * (elem - 1) // 2

print(count)

# 피드백
# prefix sum = p[j] - p[i-1]
# p[j]와 p[i-1]을 각각 M으로 나눴을 때 나머지가 동일하다면 빼기 연산 후 나머지도 0이므로 M으로 나누어 떨어진다
# 그러므로 나머지가 동일한 idx 중 임의로 2개를 선택하는 것과 같다
# nC2 = n * (n-1) // 2