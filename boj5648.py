count = 0
arr = []

a = list(map(int, input().split()))
for elem in a:
    arr.append(elem)
count += len(a)-1

while count < a[0]:
    b = list(map(int, input().split()))
    for elem in b:
        arr.append(elem)
    count += len(b)

arr = arr[1:]
arr = [int(str(x)[::-1]) for x in arr]
arr.sort()

for elem in arr:
    print(elem)