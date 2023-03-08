from collections import defaultdict

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
        
def solution(n, wires):
    answer = 100
    
    for skip in range(len(wires)):
        parent = [i for i in range(n+1)]
        d = defaultdict(int)
        for idx, wire in enumerate(wires):
            if skip == idx:
                continue
            a, b = wire[0], wire[1]
            if find(a, parent) != find(b, parent):
                union(a, b, parent)
                
        for i in range(1, len(parent)):
            d[find(i, parent)] += 1
        
        v = list(d.values())
        answer = min(abs(v[0] - v[1]), answer)
        
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

# 피드백
# d를 계산해줄 때 index를 parent[i]에서 find(i, parent)로 수정하여 문제를 해결할 수 있었다.
# 아마 유니온 파인드 문제를 풀 때 자주 겪는 실수인, '마지막에 사이클이 완성될 경우'와 같은 케이스 때문이 아닐까 싶다
# 같은 서로소 집합에 있어도 부모가 다를 수 있으므로, 부모가 아닌 루트를 기준으로 계산해주어야 한다.