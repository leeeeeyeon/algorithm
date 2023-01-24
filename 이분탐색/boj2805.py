# 내 코드
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

trees = list(map(int, sys.stdin.readline().rstrip().split()))
start = 0
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total < m:
        end = mid - 1
    
    else: # total > m
        result = mid
        start = mid + 1

print(result)

# 다른 사람 코드

# n, m = map(int, input().split())
# tree = list(map(int, input().split()))
# start, end = 1, max(tree) #이분탐색 검색 범위 설정

# while start <= end: #적절한 벌목 높이를 찾는 알고리즘
#     mid = (start+end) // 2
    
#     log = 0 #벌목된 나무 총합
#     for i in tree:
#         if i >= mid:
#             log += i - mid
    
#     #벌목 높이를 이분탐색
#     if log >= m:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

# 피드백
# - max()를 사용하면 되므로 정렬은 안해줘도 된다!
# - 최대한 덜 잘랐을 때가 정답이므로 else문에서 result 저장
# - 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
#     - 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제
#     - 이러한 유형은 재귀적으로 구현하는 것보다 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있다.