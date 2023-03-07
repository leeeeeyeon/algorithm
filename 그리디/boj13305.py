import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
liters = list(map(int, input().split()))

answer = 0
prev = 0

answer += distance[0] * liters[0]
prev = liters[0]

for i in range(1, len(distance)):
    if liters[i] * distance[i] < prev * distance[i]:
        prev = liters[i]
        answer += prev * distance[i]
    else:
        answer += prev * distance[i]

print(answer)

# 로직
# 현재(now) 정류장에서 다음(next) 정류장으로 이동하여, next ~ next+1 정류장을 가는데까지
# 1. 현재 정류장에서 next ~ next+1 거리만큼 더 충전
# 2. 다음 정류장에서 next ~ next+1 거리만큼 더 충전
# 중 더 작은 값이 무엇인지 결정하여, 더 작은 방법으로 충전한다.