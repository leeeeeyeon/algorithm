# /유니온-파인드/boj10451.py와 동일한 문제를 DFS를 사용하여 풀어보았습니다.

import sys

input = sys.stdin.readline

t = int(input())

def dfs(x):
    visited[x] = True
    for elem in graph[x]:
        if not visited[elem]:
            dfs(elem)

for _ in range(t):
    n = int(input())

    visited = [False for i in range(n+1)]
    graph = [[] for _ in range(n+1)]
    cnt = 0

    arr = [0] + list(map(int, input().split()))

    for i in range(1, len(arr)):
        graph[i].append(arr[i])

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)