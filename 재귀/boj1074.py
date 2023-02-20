import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

def z(n, r, c):
    if n==1: # 베이스 조건
        return 2 * r + c
    if r < 2 ** (n-1):
        if c < 2 ** (n-1): # 1 사분면
            return (4 ** (n-1)) * 0 + z(n-1, r, c)
        else: # 2 사분면
            return (4 ** (n-1)) * 1 + z(n-1, r, c % (2 ** (n-1)))
    else: # r / 2 >= 2 ** n
        if c < 2 ** (n-1): # 3 사분면
            return (4 ** (n-1)) * 2 + z(n-1, r % (2 ** (n-1)), c)
        else: # 4 사분면
            return (4 ** (n-1)) * 3 + z(n-1, r % (2 ** (n-1)), c % (2 ** (n-1)))

print(z(n, r, c))