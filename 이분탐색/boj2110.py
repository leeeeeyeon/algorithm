import sys

input = sys.stdin.readline

n, c = map(int, input().split())

home = []

# 입력
for _ in range(n):
    home.append(int(input()))

# 이분탐색의 기본은 정렬
home.sort()

start = 1 # 최소 거리
end = home[-1] - home[0] # 최대 거리

result = 0
# 집이 두 개라면 무조건 둘 사이의 거리
if c == 2:
    result = home[-1] - home[0]

else:
    while start < end:
        count = 1
        pre = home[0]
        mid = (start + end) // 2

        for i in range(1, n):
            if home[i] - pre >= mid:
                count += 1
                pre = home[i]
        if count >= c:
            # c개보다 공유기를 더 많이 설치할 수 있음
            # 공유기 설치 개수를 줄여야 함
            # 집 사이 거리는 커져야 함
            start = mid + 1
            result = mid
        elif count < c:
            # 공유기 설치 개수를 늘려야 함
            # 집 사이 거리는 줄어들어야 함
            end = mid

print(result)