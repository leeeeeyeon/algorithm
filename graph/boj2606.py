import sys
input = sys.stdin.readline

a = int(input()) # 컴퓨터 수, 정점
b = int(input()) # 컴퓨터 쌍의 수, 간선
graph = [[0 for _ in range(a+1)] for i in range(a+1)]
visited = [False for i in range(a+1)]
stack = []
virus = []

# 간선 정보 입력 받기
for i in range(b):
    n, m = map(int, input().split())
    graph[n][m] = 1
    graph[m][n] = 1

stack.append(1)
virus.append(1)
visited[1] = True

while len(stack) != 0:
    top = stack[-1]
    stack.pop()

    for i in range(1, a+1):
        if graph[top][i] == 1 and visited[i] == False:
            stack.append(i)
            virus.append(i)
            visited[top] = True

ans = len(list(set(virus))) -1
print(ans)

# for i in range(len(graph)):
#     print(graph[i])


# 다른 사람 코드
# from sys import stdin
# read = stdin.readline
# dic={}
# for i in range(int(read())):
#     dic[i+1] = set()
# for j in range(int(read())):
#     a, b = map(int,read().split())
#     dic[a].add(b)
#     dic[b].add(a)

# def dfs(start, dic):
#     for i in dic[start]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic)
# visited = []
# dfs(1, dic)
# print(len(visited)-1)

# 피드백
# 나는 인접 행렬 방식을 사용했는데 파이썬에선 주로 인접 리스트를 사용
# 반복문 대신 재귀를 사용하여 방문하지 않은 노드에 대해서만 DFS 적용