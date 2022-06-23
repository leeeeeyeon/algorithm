import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

print(n // m)
print(n % m)