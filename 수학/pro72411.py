from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for number in course:
        temp = []
        for order in orders:
            c = combinations(sorted(order), number)
            temp += c
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(i) for i in counter if counter[i] == max(counter.values())]
        
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))