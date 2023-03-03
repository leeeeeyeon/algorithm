import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split()) # 수빈, 동생

dq = deque()
visited = [0 for _ in range(100002)]
answer = 0

dq.append(n)

while dq:
    current = dq.popleft()
    direction = [-1, 1, current]

    if current == k:
        answer = visited[current]
        break

    for i in range(3):
        new = current + direction[i]
        if 0 <= new <= 100000 and visited[new] == 0:
            dq.append(new)
            visited[new] = visited[current] + 1

print(answer)
