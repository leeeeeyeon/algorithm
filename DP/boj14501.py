# 내 코드
n = int(input())
# 더미데이터로 크기가 n인 리스트들을 만듦
t = [-1] * n
p = [-1] * n
dp = [0] * n

# t, p 입력 받음
for i in range(n):
    t[i], p[i] = map(int, input().split())

i = 1

for i in range(1, n+1):
    print(f'[ i = {i} ]')
    result = 0
    temp = 0
    while temp < i:
        print(f'    temp = {temp}')
        if t[temp] <= i - temp:
            print(f'    t[{temp}](={t[temp]}) <= i - temp (={i-temp})')
            result += p[temp]
            temp += t[temp]
        else:
            temp += 1
    
        print(f'    result: {result}')
