import sys

input = sys.stdin.readline

t = int(input())

def find(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    rootA = find(a, parent)
    rootB = find(b, parent)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for _ in range(t):
    n = int(input())
    parent = [i for i in range(n+1)]
    arr = list(map(int, input().split()))
    edges = [(i+1, arr[i]) for i in range(len(arr))]
    cnt = 0

    for a, b in edges:
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
        else:
            cnt += 1

    print(edges)
    print(cnt)

# len(set(parent))-1을 출력하면 '틀렸습니다'가 뜨고
# find(a, parent) != find(b, parent)일 때 cnt를 증가시킨 뒤, cnt를 출력하면 '맞았습니다'가 뜬다

# 완벽하게 이해하지는 못했지만, 문제 속 그래프는 '방향' 그래프이다
# len(set(parent))-1을 출력하면, 방향이 맞지 않을 경우에도 사이클이라고 출력하기 때문에 올바르지 않은 풀이인 것 같다
