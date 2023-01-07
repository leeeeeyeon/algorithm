import sys

input = sys.stdin.readline

s = input().rstrip()
stack = []
length = 0
temp = ''

for c in s:
    if c.isdigit():
        length += 1
        temp = c
    elif c == '(':
        stack.append((temp, length -1))

        length = 0
    else:
        mul, pre = stack.pop()

        length = (int(mul) * length) + pre

print(length)