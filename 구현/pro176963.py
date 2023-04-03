from collections import defaultdict

def solution(name, yearning, photos):
    answer = []
    score = defaultdict(int)
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
        
    for photo in photos:
        total = 0
        
        for p in photo:
            total += score[p]
            
        answer.append(total)
        
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))