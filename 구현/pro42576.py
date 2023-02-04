from collections import defaultdict

def solution(participant, completion):

    members = defaultdict(int)
    
    for p in participant:
        members[p] += 1
    
    for c in completion:
        members[c] -= 1
        if members[c] == 0:
            del members[c]
        
    return list(members.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))