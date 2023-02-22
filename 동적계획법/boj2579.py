import sys

input = sys.stdin.readline

n = int(input())
stairs = [0]
dp = [0 for _ in range(n+1)]

for _ in range(n):
    stairs.append(int(input()))

dp[0] = 0
dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    dp[i] = stairs[i] + max(dp[i-2], dp[i-3] + stairs[i-1])

print(dp[n])