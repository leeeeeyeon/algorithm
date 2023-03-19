import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if hq:
            print(-heappop(hq))
        else:
            print(0)
    
    else:
        heappush(hq, -x)