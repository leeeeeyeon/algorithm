import sys

input = sys.stdin.readline

dp = [0 for _ in range(101)]

dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2

for i in range(5, 101):
    dp[i] = dp[i-1] + dp[i-5]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])