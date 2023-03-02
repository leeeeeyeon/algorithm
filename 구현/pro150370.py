from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    types = defaultdict(int)
    tyear, tmonth, tday = map(int, today.split('.'))
    
    for term in terms:
        alphabet, number = term.split()
        types[alphabet] = int(number)

    ends = []
    for i in range(len(privacies)):
        privacy = privacies[i]
        
        # 1. 유효 기간을 구한다
        date, alphabet = privacy.split()
        year, month, day = map(int, date.split('.'))
        nyear, nmonth, nday = 0, 0, 0
        
        nyear += year
        nmonth = month + types[alphabet]
        while True:
            if nmonth > 12:
                nyear += 1
                nmonth -= 12
            else:
                break
        nday = day - 1
        if nday == 0:
            nmonth -= 1
            nday = 28
            
        # 2. 유효 기간이 오늘 이전인지 구하고, 그렇다면 answer에 index를 추가한다
        if nyear < tyear:
            answer.append(i+1)
        elif nyear == tyear and nmonth < tmonth:
            answer.append(i+1)
        elif nyear == tyear and nmonth == tmonth and nday < tday:
            answer.append(i+1)
        
    return answer

print(solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution('2020.01.01', ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

# 1트 - 1번 테케 빼고 다 실패, 수집 일자가 12월이고 유효 기간이 12의 배수일 때 예외 조건 추가
# 2트 - 1번 테케 빼고 다 실패, answer.append() 조건 다시 작성
# 3트 - 13,14,17번 테케 실패, nmonth를 //와 % 연산으로 재계산하는 것을 반복문으로 12씩 빼는 방법으로 변경

# 피드백
# 문제에 주어진대로 꼼꼼히 구현하면 된다
# 년도나 달이 바뀔 때 예외 상황을 주의하자