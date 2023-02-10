import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(str(input().rstrip()))
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    deq = deque(arr)
    flag = False
    rev = 0

    for elem in p:
        if elem == 'R':
            rev += 1
        elif elem == 'D':
            if len(deq) < 1 or arr == ['']:
                flag = True
                print('error')
                break
            else:
                if rev % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()

    if not flag:
        if rev % 2 == 0:
            print('[' + ','.join(deq) + ']')
        else:
            deq.reverse()
            print('[' + ','.join(deq) + ']')