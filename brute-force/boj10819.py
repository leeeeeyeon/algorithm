import sys
import itertools

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

per = list(itertools.permutations(a, n))
# print(per)

ans = 0
for li in per:
    temp = 0
    for i in range(len(li)-1):
        temp += abs(li[i]-li[i+1])
    if temp > ans:
        ans = temp

print(ans)