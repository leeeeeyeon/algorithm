import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # n - 집의 개수
    # m - 도둑이 훔칠 연속된 집의 개수
    # k - 방범 장치가 작동하는 최소 돈의 양
    n, m, k = map(int, input().split())
    house = list(map(int, input().split()))

    # 연속된 집의 개수가 주어졌으므로 슬라이딩 윈도우 기법을 사용하자
    start = 0
    count = 0
    result = 0

    # 최초 경우에 대하여
    for i in range(m):
        result += house[i]
    if result < k:
        count += 1

    # n == m인 경우에는 loop를 돌 필요가 없다!
    # n == m인 경우에 loop를 돌면 항상 조건을 만족하므로 count = n이 나옴
    if n != m:
        start += 1
        # 그 이후 경우에 대하여
        while start != n:
            # index out of range 방지
            # start > (n - m)일 경우
            if start > (n - m):
                result += (house[(start + (m - 1)) % n] - house[start - 1])
                if result < k:
                    count += 1
            # 일반적인 경우
            else:
                result += (house[start + (m - 1)] - house[start - 1])
                if result < k:
                    count += 1

            start += 1

    print(count)