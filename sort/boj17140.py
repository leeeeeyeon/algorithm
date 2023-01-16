import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

def rc():
    max_len = 0
    for j in range(len(A)):
        a = [i for i in A[j] if i!= 0]
        a = Counter(a).most_common()
        a.sort(key = lambda x: (x[1], x[0]))

        A[j] = []
        for key, value in a:
            A[j].append(key)
            A[j].append(value)
        
        if max_len < len(a) * 2:
            max_len = len(a) * 2

    for j in range(len(A)):
        for k in range(max_len - len(A[j])):
            A[j].append(0)
        A[j] = A[j][:100]

for i in range(101):
    try:
        if A[r-1][c-1]==k:
            print(i)
            break
    except:
        pass
    
    if len(A) < len(A[0]):
        A = list(zip(*A))
        rc()
        A = list(zip(*A))
    else:
        rc()

else:
    print(-1)