import sys

input = sys.stdin.readline

x, y = map(int, input().split()) # x월 y일

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

prev = sum([month[i] for i in range(1, x)])
diff = prev + y - 1

print(day[diff % 7])