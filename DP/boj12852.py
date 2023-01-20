import sys

input = sys.stdin.readline

dp = [0, 0]
num = [0, [1]]
n = int(input())

for i in range(2, n+1):
    dp.append(dp[i-1] + 1)
    num.append([i] + num[i-1])

    if i%3==0 and dp[i//3]+1<dp[i]:
        dp[i] = dp[i//3]+1
        num[i] = [i] + num[i//3]
    if i%2==0 and dp[i//2]+1<dp[i]:
        dp[i] = dp[i//2]+1
        num[i] = [i] + num[i//2]

print(dp[n])
for elem in num[n]:
    print(elem, end = ' ')