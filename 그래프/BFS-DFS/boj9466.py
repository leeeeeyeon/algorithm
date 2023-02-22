import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

t = int(input())

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    elem = graph[x][0]

    if visited[elem]:
        if elem in cycle: # 사이클을 이뤘을 때
            result += cycle[cycle.index(elem):]
        return
    else:
        dfs(elem)

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]

    arr = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    result = [] # 팀을 이룬 학생들

    for i in range(1, n+1):
        graph[i].append(arr[i])

    for i in range(1, n+1):
        if not visited[i]:
            cycle = [] # 번호마다 사이클 여부를 판단하기 위해 초기화
            dfs(i)

    print(n-len(result))

# 피드백
# cycle, result 두 개의 리스트가 필요하다
# cycle - 각 번호마다 해당 번호를 루트로 사이클이 형성되는지 확인한다
# result - 사이클에 있는 번호들을 저장한다
 