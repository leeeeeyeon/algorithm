import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
p = permutations(num, m)

for elem in p:
    for e in elem:
        print(e, end=' ')
    print()