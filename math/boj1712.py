import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

if b - c >= 0:
    print(-1)

else:
    print(a // (c-b) + 1)