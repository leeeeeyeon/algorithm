import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]

# 초기값 세팅
for i in range(1, 31):
    for j in range(1, 31):
        # 서쪽 사이트가 1개일 경우
        if i == 1:
            dp[i][j] = j
        # 서쪽 사이트가 더 많은 경우 고려하지 x
        elif i > j:
            dp[i][j] = 0
        # 양쪽 사이트 개수 동일
        elif i == j:
            dp[i][j] = 1

        else:
            for k in range (i-1, j):
                dp[i][j] += dp[i-1][k]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])

# 다른 사람 코드
# 1) 조합을 사용
# import math

# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
#     print(bridge)

# 2) DP
# import sys
# input = sys.stdin.readline

# t = int(input())

# dp = [[0 for _ in range(30)]for _ in range(30)]
# for i in range(1, 30):
#     for j in range(1, 30):
#         if i == 1:
#             dp[i][j] = j
#         elif i == j:
#             dp[i][j] = 1
#         else:
#             if j > i:
#                 dp[i][j] = dp[i-1][j-1]+dp[i][j-1]

# for _ in range(0, t):
#     n, m = map(int, input().split(' '))
#     print(dp[n][m])

# 피드백
# 조합은 생각을 못했다 ... 알고리즘도 ... 수학이다 ... ^_ㅠ
# DP 점화식은 내가 푼 것보다 'dp[i][j] = dp[i-1][j-1]+dp[i][j-1]' 이게 더 깔끔
