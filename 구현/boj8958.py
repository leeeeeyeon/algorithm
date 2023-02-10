import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    scores = []
    score = 0
    s = input().rstrip()
    for elem in s:
        if elem == 'O':
            score += 1
            scores.append(score)
        else:
            score = 0
    print(sum(scores))