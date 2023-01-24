import sys
from itertools import combinations

input = sys.stdin.readline

# n - 도시의 크기, m - 치킨집의 개수
n, m = map(int, input().split())

board = [] # 도시
chickens = [] # 치킨집 좌표
homes = [] # 집 좌표
INF = 1e9

# 도시의 정보
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# 집과 치킨집의 좌표를 배열에 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))
        
# 조합으로 치킨집 M개를 고른다
c = list(combinations(chickens, m))

# 집의 치킨 거리
def home_chicken(home, chickens):
    result = INF
    for chicken in chickens:
        dist = abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

        if dist < result:
            result = dist

    return result

# 도시의 치킨 거리
def town_chicken(homes, chickens):
    dist = 0

    for home in homes:
        dist += home_chicken(home, chickens)

    return dist

ans = INF
for elem in c:
    temp = town_chicken(homes, elem)
    if temp < ans:
        ans = temp

print(ans)