# 내 코드
import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = 1e9

v, e = map(int, input().split()) # 정점의 개수 v와 간선의 개수 e
k = int(input()) # 시작 노드

graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

# 간선 정보 입력 받기
for i in range(e):
    a, b, c = map(int, input().split()) # a부터 b까지 가는 가중치 c
    graph[a].append((b, c))

print(graph)

def dijkstra(start):
    q = [] # 우선순위 큐
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])