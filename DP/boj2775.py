import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input()) # k층
    n = int(input()) # n호

    # dp 배열 초기화
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    dp[0] = [i for i in range(n+1)]
    for elem in dp:
        elem[1] = 1

    # 점화식 계산
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[k][n])