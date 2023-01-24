# 내 코드
n = input()

arr = [0] * 10

for elem in n:
    if int(elem) == 9:
        arr[6] += 1
    else:
        arr[int(elem)] += 1

if arr[6] % 2 == 0:
    arr[6] = arr[6] // 2
else:
    arr[6] = arr[6] // 2 + 1

result = max(arr)

print(result)

# 다른 사람 코드
# n = input()
# a = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
# for i in range(len(n)):
#     if n[i] in ['6', '9']:
#         a['6'] += 1
#     else:
#         a[n[i]] += 1
# if a['6'] % 2 == 0:
#     a['6'] = a['6'] // 2
# else:
#     a['6'] = a['6'] // 2 + 1
# print(max(a.values()))

# 피드백
# - 원리는 동일한데 max를 계산할 때 // 연산을 해주니 실패하고, max 계산 전 // 연산을 해주니 성공하였다 >:( )
