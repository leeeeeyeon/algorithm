import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

d = defaultdict(int)

for _ in range(n):
    name, extension = input().rstrip().split('.')
    d[extension] += 1

keys = list(d.keys())
keys.sort()

for key in keys:
    print(f'{key} {d[key]}')