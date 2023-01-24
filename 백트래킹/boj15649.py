import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

# 백트래킹으로 푼 코드
arr = [0 for i in range(m)]
issued = [False for i in range(n+1)]

def func(k):
    if k == m:
        for elem in arr:
            print(elem, end=' ')
        print()
        return

    for i in range(1, n+1):
        if not issued[i]:
            arr[k] = i
            issued[i] = True
            func(k+1)
            issued[i] = False

func(0)

# 순열로 푼 코드
# p = permutations(num, m)

# for elem in p:
#     for e in elem:
#         print(e, end=' ')
#     print()