import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0 for i in range(m)]
issued = [False for i in range(n+1)]

def func(k, start):
    if k == m:
        for elem in arr:
            print(elem, end=' ')
        print()
        return

    for i in range(start, n+1):
        if not issued[i]:
            arr[k]=i
            issued[i] = True
            func(k+1, i+1)
            issued[i] = False

func(0, 1)