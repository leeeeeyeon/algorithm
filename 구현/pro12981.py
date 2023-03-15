def solution(n, words):
    answer = []
    done = set()
    done.add(words[0])
    
    for i in range(1, len(words)):
        word = words[i]
        if word in done or word[0] != words[i-1][-1]:
            answer.append(i % n + 1) # 번호
            answer.append(i // n + 1) # 차례
            break
        done.add(word)
        
    if not answer: # 탈락자가 발생하지 않을 경우
        answer = [0, 0]
        
    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))