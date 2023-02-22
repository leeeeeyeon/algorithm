import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0], dp[1] = 1, 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n])

# 피드백
# 점화식: DP[i] = DP[i-1] + DP[i-2]

# 나는 이진수 앞이나 뒤에 00, 1을 붙이는 것을 생각했는데, 뒤에 붙이는 경우만 생각해주면 된다
# 출력할 때 나머지 연산을 하면 메모리 초과가 뜬다
# DP 리스트에 저장할 때 나머지 연산을 해야 한다
