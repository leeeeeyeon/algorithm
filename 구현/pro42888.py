from collections import defaultdict

def solution(records):
    answer = []
    d = defaultdict(str)
    
    for record in records:
        arr = record.split(' ')
        action = arr[0]
        
        if action == 'Enter':
            uid, nickname = arr[1], arr[2]
            answer.append([uid, '님이 들어왔습니다.'])
            d[uid] = nickname
        elif action == 'Leave':
            uid = arr[1]
            answer.append([uid, '님이 나갔습니다.'])
        else: # action == 'Change'
            uid, nickname = arr[1], arr[2]
            d[uid] = nickname
    
    for i in range(len(answer)):
        answer[i] = d[answer[i][0]] + answer[i][1]
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))