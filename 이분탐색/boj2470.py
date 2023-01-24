import sys

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n-1
mid = int(1e10)
answer = [0, n-1]

while start < end:
    sum = arr[start] + arr[end]
    if abs(sum) < abs(mid):
        mid = sum
        answer[0]=start
        answer[1]=end

    if sum < 0:
        start += 1
    elif sum > 0:
        end -= 1
    else:
        break
print(arr[answer[0]], arr[answer[1]])