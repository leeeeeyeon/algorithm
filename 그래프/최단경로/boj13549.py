import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 1e6

n, k = map(int, input().split())
visited = [INF for _ in range(100001)]
heap = []
answer = -1
heappush(heap, (0, n)) # 시간, 노드 순
visited[n] = 0

while heap:
    cost, node = heappop(heap)

    adjacent = [(1, node-1), (1, node+1), (0, 2*node)]

    if visited[node] < cost:
        continue

    for dist, next in adjacent:
        ncost = cost + dist
        if 0 <= next <= 100000 and ncost < visited[next]:
                visited[next] = ncost
                heappush(heap, (ncost, next))
                
print(visited[k])