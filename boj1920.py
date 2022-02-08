import sys

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()

m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

for elem in b:
    ans = binary_search(a, elem, 0, n-1)
    if ans == None:
        print(0)
    else:
        print(1)
