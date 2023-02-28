def find(x, parent):
    if x == parent[x]:
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

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    
    for _ in range(2):
        for i in range(len(computers)):
            for j in range(len(computers[0])):
                if computers[i][j] == 1 and find(i, parent) != find(j, parent):
                    union(i, j, parent)

    return len(set(parent))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 피드백
# 백준 11724번과 똑같은 이유로 틀렸다
# 마지막에 사이클이 완성될 경우가 반례이다