import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

d = defaultdict(int)
answer = 0

for _ in range(n):
    word = input().rstrip()

    for i in range(len(word)):
        d[word[i]] += 10 ** (len(word)-i-1)

arr = sorted(list(d.keys()), key = lambda x: d[x], reverse = True)

for i in range(len(arr)):
    answer += d[arr[i]] * (9-i)

print(answer)