import sys

input = sys.stdin.readline

n = int(input())

health = []
happy = []
dp = [[0 for _ in range(101)] for _ in range(n+1)]

health = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, 101):
        if j-health[i] >= 0:
            dp[i][j] = max(dp[i-1][j-health[i]]+ happy[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])