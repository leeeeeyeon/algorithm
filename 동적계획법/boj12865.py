import sys

input = sys.stdin.readline

# 물품의 수, 최대 무게
n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
weight = [0 for _ in range(101)]
value = [0 for _ in range(101)]

for i in range(n):
    w, v = map(int, input().split())
    weight[i+1] = w
    value[i+1] = v

for i in range(1, n+1):
    for j in range(1, k+1):
        if j<weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

print(dp[n][k])