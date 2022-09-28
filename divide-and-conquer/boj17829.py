import sys

input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)] # 행렬 초기화

for i in range(n):
        arr[i] = list(map(int, input().split()))

def pooling(size, x, y):
    mid = size // 2
    if size == 2:
        return sorted([arr[x][y], arr[x+mid][y], arr[x][y+mid], arr[x+mid][y+mid]])[-2]

    lt = pooling(mid, x, y)
    lb = pooling(mid, x, y+mid)
    rt = pooling(mid, x+mid, y)
    rb = pooling(mid, x+mid, y+mid)

    ans = [lt, lb, rt, rb]

    return sorted(ans)[-2]

print(pooling(n, 0, 0))