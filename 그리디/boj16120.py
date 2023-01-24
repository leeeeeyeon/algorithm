import sys

arr = []

string = sys.stdin.readline().rstrip()

for i in range(len(string)):
    arr.append(string[i])
    # print(''.join(arr)[-4:])
    if 'PPAP' == ''.join(arr[-4:]):
        for _ in range(4):
            arr.pop()
        arr.append('P')

if arr[0] == 'P':
    arr.pop()

if not arr:
    print('PPAP')
else:
    print('NP')