from collections import defaultdict

def solution(begin, target, words):
    answer = 1e6
    visited = defaultdict(bool)
    
    if target not in words: # 반환할 수 없는 경우에는 0을 리턴
        return 0

    stack = []
    stack.append((begin, 0))
    visited[begin] = True
    
    while stack:
        current, cnt = stack.pop()
        
        if current == target:
            answer = min(answer, cnt)
        
        arr = []
        for word in words:
            temp = 0
            for i in range(len(current)):
                if current[i] != word[i]:
                    temp += 1
            if temp == 1:
                arr.append(word)
        
        for elem in arr:
            if not visited[elem]:
                stack.append((elem, cnt + 1))
                visited[elem] = True
                
    if answer >= 1e5:
        return 0
    else:
        return answer
    
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# 피드백
# 알파벳이 하나만 차이 날 때를 조건문으로 if(len(set(begin)-set(word))) == 1로 해서 테케 3번에서 틀렸다
# 위와 같이 할 경우 'hot', 'tdo'도 True가 되므로 한 글자씩 비교해주어야 한다
# 딕셔너리 형태의 visited 배열을 사용하지 않고, 인덱스를 사용하여 리스트로 방문 여부를 관리할 수 있다.

# 다른 사람 코드
# from collections import deque

# def solution(begin, target, words):
#     answer = 0
#     q = deque()
#     q.append([begin, 0])
#     V = [ 0 for i in range(len(words))]
#     while q:
#         word, cnt = q.popleft()
#         if word == target:
#             answer = cnt
#             break        
#         for i in range(len(words)):
#             temp_cnt = 0
#             if not V[i]:
#                 for j in range(len(word)):
#                     if word[j] != words[i][j]:
#                         temp_cnt += 1
#                 if temp_cnt == 1:
#                     q.append([words[i], cnt+1])
#                     V[i] = 1
                    
#     return answer