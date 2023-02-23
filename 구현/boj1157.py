import sys
from collections import defaultdict

input = sys.stdin.readline

s = input().rstrip()
s = s.upper()
d = defaultdict(int)

for elem in s:
    d[elem] += 1

result = []
mx = max(d.values())
for key in d.keys():
    if d[key] == mx:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')