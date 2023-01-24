import sys
import math

input = sys.stdin.readline

n = int(input())

k = int(math.log10(n))+1

if k == 1:
    print(n)

else:
    ans = 0
    for i in range(k):
        ans += i * 9 * math.pow(10, i-1)

    ans += k * (n - math.pow(10, k - 1) + 1)

    print(int(ans))