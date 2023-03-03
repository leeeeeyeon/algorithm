import sys

input = sys.stdin.readline

n = int(input()) # 악보의 개수

diff = list(map(int, input().split())) # 1~N번 악보의 난이도
q = int(input()) # 질문의 개수
dp = [0 for _ in range(n)]

for i in range(1, n):
    dp[i] = dp[i-1]+1 if diff[i] < diff[i-1] else dp[i-1]

for _ in range(q):
    x, y = map(int, input().split())

    print(dp[y-1] - dp[x-1])
