import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
    q = deque([])
    answer = 0

    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        q.append((i, arr[i]))

    while q:
        mx = max([elem[1] for elem in q])
        x, y = q.popleft() # 순서, 중요도

        if y == mx:
            answer += 1
            if x == m:
                print(answer)
                break
            else:
                continue
        else:
            q.append((x, y))