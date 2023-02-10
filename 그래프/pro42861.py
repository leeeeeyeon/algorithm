def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent_a = find(parent, a)
    parent_b = find(parent, b)
    
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_b] = parent_a

def solution(n, costs):
    answer = 0
    parent = []
    
    for i in range(n):
        parent.append(i)

    costs.sort(key = lambda x: x[2])
    
    for cost in costs:
        if find(parent, cost[0]) != find(parent, cost[1]):
            union(parent, cost[0], cost[1])
            answer += cost[2]
            
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))