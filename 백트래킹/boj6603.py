import sys

input = sys.stdin.readline

def func(s, start):
    if len(s) == 6:
        print(*s)
        return
    for i in range(start, len(arr)):
        if not visited[i]:
            # 원소가 비었거나(최초) or 그렇지 않을 때는 들어올 원소가 마지막 원소보다 커야함
            if not s or (s and arr[i] > s[-1]):
                s.append(arr[i])
                visited[i] = True
                func(s, start+1)
                s.pop()
                visited[i] = False

while True:
    arr = list(map(int, input().split()))
    if arr == [0]: # 입력의 마지막 줄에는 0이 하나 주어진다
        break
    k = arr[0]
    arr = arr[1:]
    visited = [False for _ in range(len(arr))]
    func([], 0)
    print()
