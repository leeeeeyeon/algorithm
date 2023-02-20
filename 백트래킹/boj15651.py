import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 같은 수를 여러 번 골라도 된다
def func(s):
    if len(s) == m:
        print(*s)
        return
    for i in range(1, len(numbers)):
        s.append(numbers[i])
        func(s)
        s.pop()

numbers = [i for i in range(n+1)]
func([])