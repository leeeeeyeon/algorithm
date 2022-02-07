n = int(input())
arr = []
for _ in range(n):
    input_data = input().split() 
    arr.append((int(input_data[0]), input_data[1]))

arr.sort(key=lambda a: a[0])

for i in range(len(arr)):
    print(arr[i][0],arr[i][1])