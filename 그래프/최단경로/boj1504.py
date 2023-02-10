import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split()) # 정점, 간선의 개수

graph = [[] for _ in range(n+1)]

# 입력
for _ in range(e):
    # a에서 b로 가는 거리가 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    d = [INF for _ in range(n+1)]
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        # 인접 노드를 탐색
        for node, w in graph[now]:
            cost = dist + w
            if cost < d[node]:
                d[node] = cost
                heapq.heappush(q, (cost, node))

    return d

one = dijkstra(1)
v1_arr = dijkstra(v1)
v2_arr = dijkstra(v2)

first = one[v1] + v1_arr[v2] + v2_arr[n]
second = one[v2] + v2_arr[v1] + v1_arr[n]

result = min(first, second)

print(result if result < INF else -1)
