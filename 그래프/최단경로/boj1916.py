import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    # a에서 출발해서 b까지 가는데 c라는 비용이 소요됨
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        # 처리된 적 있는 노드
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 노드
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])