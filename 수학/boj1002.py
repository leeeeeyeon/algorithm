import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2: # 동심원이며 반지름이 같으면 접점이 무한대
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1 - r2): # 외접 또는 내접이면 접점이 1개
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2): # 접점이 2개
        print(2)
    else:
        print(0)