import sys

input = sys.stdin.readline

n = int(input())

card = [0] + list(map(int, input().split()))

dp = [card[i] for i in range(len(card))]

for i in range(2, n+1):
    mx = 0
    for j in range(1, i):
        mx = max(mx, dp[j]+card[i-j])
    
    dp[i] = max(card[i], mx)

print(dp[-1])