# 내 코드
n = int(input())
rings = list(map(int, input().split()))
answer = []

# 분수를 약분하는 함수
def reduce(elem): # n/m
    temp = ''
    n, m = map(int, elem.split('/'))
    for i in range(max(n, m), 1, -1):
        if n % i == 0 and m % i == 0:
            temp = str(n // i) + '/' + str(m // i)
            return temp
    if temp == '': # 최대공배수가 존재하지 않음 > 그 자체로 기약분수
        return elem

for i in range(1, n):
    temp = ''
    if rings[0] % rings[i] == 0:
        temp = str(rings[0] // rings[i]) + '/1'
        temp = reduce(temp)
        answer.append(temp)
    else: # 최소공배수 // rings [i]
        mul = rings[0] * rings[i]
        for j in range(mul, 1, -1):
            if mul % rings[0] == 0 and mul % rings[i] == 0:
                temp = str(mul // rings[i]) + '/' + str(mul // rings[0])
                break
        temp = reduce(temp)
        answer.append(temp)

for elem in answer:
    print(elem)

# 다른 사람 코드
# import sys

# def gcd(n1, n2):
#     while n2 :
#         n1, n2 = n2, n1 % n2
#     return n1

# N = int(sys.stdin.readline())
# rings = list(map(int,  sys.stdin.readline().split()))
# for i in range(1, N):
#     gcd_val = gcd(rings[0], rings[i])
#     print('{0}/{1}'.format(rings[0]//gcd_val, rings[i]//gcd_val))

# 피드백
# 최대공약수를 구하는 함수에서 while문을 쓰면 더 간략해진다
# reduce()와 23~28번째 줄 겹침 > reduce() 함수를 사용해 코드를 짧게 쓸 수 있었음
# for 문 안에서 if-else문 나눌 필요 없었음!
# '+' 연산자 대신 format() 함수를 이용하여 한 줄로 출력 가능
# 맞았긴 했지만 아쉬운 점이 많은 코드 :(