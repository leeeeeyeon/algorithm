import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1, n+1):
    dp[1][i] = 1
    if k > 1:
        dp[2][i] = i+1

for i in range(1, k+1):
    dp[i][1] = i

if k > 1 and n > 1:
    for i in range(2, k+1):
        for j in range(2, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[k][n] % 1000000000)

# 피드백
# n이나 k가 1일 때도 주의하자 (IndexError)
