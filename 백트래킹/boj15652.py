import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def func(s):
    if len(s) == m:
        print(*s)
        return
    for i in range(1, len(numbers)):
        if s and numbers[i] < s[-1]:
            continue
        s.append(numbers[i])
        func(s)
        s.pop()
    
numbers = [i for i in range(0, n+1)]
func([])