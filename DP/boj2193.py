# 내 코드
n = int(input())

dp = [0]*90
dp[0] = 1
dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])

# 다른 사람 코드
# s = [0, 1, 1]
# for i in range(3, 91):
#   s.append(s[i - 2] + s[i - 1])
# n = int(input())
# print(s[n])

# 피드백
# 점화식 : dp[i] = dp[i-1] + dp[i-2]