from itertools import permutations

def solution(k, dungeons):
    answer = 0
    numbers = [i for i in range(len(dungeons))]
    p = permutations(numbers, len(dungeons))
    
    for elem in p:
        temp = k
        cnt = 0
        for seq in elem:
            if temp >= dungeons[seq][0]:
                temp -= dungeons[seq][1]
                cnt += 1
            else:
                break
        answer = max(cnt, answer)
        
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))