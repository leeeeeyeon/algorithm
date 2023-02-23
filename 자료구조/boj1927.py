import sys
import heapq

input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print('0')
    else:
        heapq.heappush(hq, x)