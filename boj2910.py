a, b = input().split()

arr = list(map(int, input().split()))
res = list(set([(x, arr.count(x)) for x in arr]))
order = list(dict.fromkeys(arr))
res.sort(key= lambda x:(-x[1], order.index(x[0])))

ans = []
for elem in res:
    for _ in range(elem[1]):
        ans.append(elem[0])

for elem in ans:
    print(elem, end=' ')