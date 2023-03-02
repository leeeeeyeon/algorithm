from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(int)
    musics = defaultdict(list)
    
    for i in range(len(genres)):
        d[genres[i]] += plays[i]
        musics[genres[i]] += [(i, plays[i])]

    for key in sorted(d.keys(), key = lambda x: -d[x]):
        arr = musics[key]
        arr.sort(key = lambda x: (-x[1], x[0]))
        
        if len(arr) == 1:
            answer.append(arr[0][0])
        else:
            for i in range(2):
                answer.append(arr[i][0])
    return answer

# 피드백
# d.keys()를 리스트로 형 변환하지 않아도 정렬을 할 수 있다는 것을 알게 되었다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# genres와 plays의 길이가 1일 때 런타임 에러가 발생했다. 문제를 꼼꼼히 읽자 !