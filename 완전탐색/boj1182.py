import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
for i in range(1, len(arr)+1):
    combi = combinations(arr, i)

    for c in combi:
        if sum(c) == s:
            answer += 1

print(answer)