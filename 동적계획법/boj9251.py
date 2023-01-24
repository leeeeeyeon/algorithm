import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            # max(dp[i-1][j], dp[i][j-1])가 아니라 dp[i-1][j-1]로 해야됨 !!!!!
            
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(b)][len(a)])