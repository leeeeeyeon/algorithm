import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
dp = [1] + [0 for _ in range(k)]
for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] += dp[j-coin]

print(dp[k])