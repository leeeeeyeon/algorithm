import sys
input = sys.stdin.readline

a = int(input()) # 컴퓨터 수, 정점
b = int(input()) # 컴퓨터 쌍의 수, 간선
graph = [[] for i in range(a+1)]
distance = [[] * (a+1)]
visited = [False for i in range(a+1)]

# 간선 정보 입력 받기
for i in range(b):
    n, m = map(int, input().split())
    graph[n].append(m)

for elem in graph[1]:
    visited[elem] = True
    for i in graph[elem]:
        if not visited[i]:
           graph[1].append(i)
           visited[elem] = True

print(graph)
print(len(graph[1]))