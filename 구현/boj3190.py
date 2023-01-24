import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 보드의 크기

k = int(input()) # 사과의 개수
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    apples.append((x, y))

l = int(input()) # 방향 변환
move_sec = []
move_dir = []
for _ in range(l):
    s, d = input().split()
    s = int(s)
    move_sec.append(s)
    move_dir.append(d)

d = deque() 
cnt = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 초기 좌표를 덱에 넣고 시작
cur = (1, 1)
dir_idx = 0
dir = direction[dir_idx]
d.append(cur)

while(True):
    cnt += 1
    x, y = cur[0], cur[1]
    dir_x, dir_y = dir[0], dir[1]
    next = (x + dir_x, y + dir_y)

    # 벽에 부딪히거나 자신의 몸에 부딪힘
    if next[0] > n or next[0] < 1 or next[1] > n or next[1] < 1 or next in d:
        break

    # 계속 진행
    d.append(next) # 오른쪽에 삽입, pop은 왼쪽에서 해야함
    if next not in apples: # 이동한 칸에 사과가 없다면
        d.popleft()
    else:
        apples.remove(next)

    cur = next

    # 방향 전환
    if cnt in move_sec:
        idx = move_sec.index(cnt)
        move = move_dir[idx]
        if move == 'D':
            dir_idx = (dir_idx + 1) % 4
            dir = direction[dir_idx]
        else: # move == 'L'
            dir_idx = (dir_idx - 1) % 4
            dir = direction[dir_idx]

print(cnt)