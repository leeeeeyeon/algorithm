import sys

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

dp[0] = [0 for _ in range(10)]
dp[1] = [1 for _ in range(10)]

for i in range(2, n+1):
    dp[i][0] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n])%10007)

# 피드백
# 앞에서부터 숫자를 생각하면 규칙을 찾기 어렵다
# 끝나는 숫자를 기준으로 표를 만들면 규칙을 찾기 쉽다
# ex) 0으로 끝나는 수, 1로 끝나는 수 ...