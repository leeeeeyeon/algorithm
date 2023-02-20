import sys

input = sys.stdin.readline

arr = list(input().rstrip().split(' '))

if arr[0] == '':
    arr = arr[1:]

print(len(arr))