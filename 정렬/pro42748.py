def solution(array, commands):
    answer = []
    
    for command in commands:
        # i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, K번째 수
        i, j, k = command[0], command[1], command[2]
        # 1.배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬
        temp = sorted(array[i-1:j])
        # 2.  k번째에 있는 수를 구한다
        ans = temp[k-1]
        
        answer.append(ans)
    return answer

# 다른 사람 코드
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
