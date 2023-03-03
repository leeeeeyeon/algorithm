import sys
from collections import deque, defaultdict

input = sys.stdin.readline

s = ''
answer = -1
visited = defaultdict(int)
dq = deque()
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for _ in range(3):
    s += ''.join(list(input().split()))

dq.append(s)
visited[s] = 0

while dq:
    current = dq.popleft()

    if current == '123456780':
        answer = visited[current]
        break

    idx = current.index('0')
    x, y = idx // 3, idx % 3 # 0의 좌표
    
    for i in range(4):
        new = list(current)
        nx, ny = x + direction[i][0], y + direction[i][1]
        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue
        new[idx], new[nx*3+ny] = new[nx*3+ny], new[idx]
        new = ''.join(new)
        if new in visited.keys():
            continue

        dq.append(new)
        visited[new] = visited[current] + 1

print(answer)

# 피드백
# 메모리 제한이 32MB로 매우 작다
# 2차원 리스트를 문자열 형태로 관리하자
# 그러면 예제 입력 1은 103425786이 된다.
# 문자열에서의 인덱스를 idx라고 하면, 이 수의 2차원 리스트에서의 좌표는 (idx//3, idx%3)이다.

# 문자열의 요소를 변경할 때는 list로 형변환을 해주어야 한다
# 방문 여부를 딕셔너리 형태로 관리한다