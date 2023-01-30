import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

# index out of range 방지
arr += [0 for _ in range(int(1e5))]

# 투 포인터 알고리즘
left = 0
right = 0
cur = 0
result = 0

# 1. 부분합이 S 이상이 될 때까지 오른쪽 포인터를 움직인다.
while cur < s:
    if right <= n-1:
        cur += arr[right]
        right += 1
    # 2. right이 n-1보다 커지면 부분합을 만드는 것이 불가능하다는 뜻
    else:
        break

# 길이를 계산
result = right - left

# 부분합을 만드는 것이 불가능한 경우
if result == 0 or cur < s:
    print(0)
# 부분합을 만드는 것이 가능한 경우
else:
    # 왼쪽 포인터가 마지막 원소에 다다를 때까지
    while left <= n-1:
        # 부분합을 계산
        cur -= arr[left]
        cur += arr[right]
        left += 1

        if cur < s:
            right += 1
            continue
        # S 이상이지만 길이를 줄일 수 있으면 길이를 계속 줄임
        else:
            while cur-arr[right] >= s:
                cur -= arr[right]
                result -= 1
                right -= 1
        right += 1

    print(result)

# 다른 사람 코드 - 나보다 메모리가 약 3배가 작다
# left, right = 0, 0 # 두 개의 포인터는 0에서 부터 시작
# sum = 0 # 합을 저장할 변수
# min_length = sys.maxsize # 먼저 최대 길이로 지정

# while True:
#     # 만약 총 합이 S가 넘는다면, left를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
#     if sum >= s:
#         min_length = min(min_length, right - left)
#         sum -= arr[left]
#         left += 1
#     elif right == n:
#         break
#     # 만약 총합이 S를 넘지 않는다면, right 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을때까지 더함
#     else:
#         sum += arr[right]
#         right += 1

# if min_length == sys.maxsize:
#     print(0)
# else:
#     print(min_length)