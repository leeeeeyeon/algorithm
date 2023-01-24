import sys

input = sys.stdin.readline

n = int(input())

ground = [[0] * n for _ in range(n)]

for i in range(n):
    ground[i] = list(map(int, str(input().rstrip())))

def dfs(x, y):
    global building
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if ground[x][y] == 1:
        building += 1
        ground[x][y] = 0
        dfs(x-1, y) # 위
        dfs(x+1, y) # 아래
        dfs(x, y-1) # 왼쪽
        dfs(x, y+1) # 오른쪽
        return True

    return False

result = 0
arr = []
building = 0

for i in range(n):
    for j in range(n):
        building = 0
        if dfs(i, j) == True:
            result += 1
            arr.append(building)

print(result) # 단지 수 출력

# 단지 내 집의 수 출력
arr.sort()
for i in range(len(arr)):
    print(arr[i])