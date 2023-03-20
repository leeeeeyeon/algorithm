from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        
    dq = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if city in dq:
            answer += 1
            dq.remove(city)
        else:
            answer += 5
        if len(dq) == cacheSize:
            dq.popleft()   
        dq.append(city) 
            
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
