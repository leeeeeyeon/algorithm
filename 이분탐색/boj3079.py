import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start = 1
end = m * arr[-1]
mx = 0

while start <= end:
    temp = []
    mid = (start + end) // 2
    if start == mid:
        start += 1
        continue

    for elem in arr:
        temp.append(mid // elem)
    
    mx = sum(temp)

    if mx >= m:
        end = mid
    else:
        start = mid

print(mid)
