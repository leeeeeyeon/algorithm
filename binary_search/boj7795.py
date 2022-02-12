# 시간초과 !!!
def binary_search(arr, target, start, end):
    if start > end:
        return (start + end) // 2
    mid = (start + end) // 2
    if target == mid:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr,target, mid+1, end)     

t = int(input())

for _ in range(t):
    n, m = input().split()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for elem in a:
        temp = [x for x in b if x < elem]
        count += len(temp)

    print(count)