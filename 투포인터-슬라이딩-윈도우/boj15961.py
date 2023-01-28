import sys
from collections import defaultdict

input = sys.stdin.readline

# 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
n, d, k, c = map(int, input().split())

sushi = []
left = 0
right = 0
ans = 0

for _ in range(n):
    sushi.append(int(input()))

# 원형 리스트이므로 리스트 두 개를 합쳐서 사용
# %를 사용하지 않고 편하게 인덱스 접근 가능!
sushi += sushi

belt = defaultdict(int)

# 보너스 초밥은 먹고 시작
belt[c] += 1

while right < k:
    belt[sushi[right]] += 1
    right += 1

while left < n:
    belt[sushi[left]] -= 1
    if belt[sushi[left]] == 0:
        del belt[sushi[left]]
    belt[sushi[right]] += 1

    ans=max(ans, len(belt))
    left += 1
    right += 1

print(ans)