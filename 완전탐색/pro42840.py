def solution(answers):
    result = [0] * 3
    arr = [[1,2,3,4,5],
           [2,1,2,3,2,4,2,5],
           [3,3,1,1,2,2,4,4,5,5]
          ]
    
    for j in range(len(arr)):
        elem = arr[j]
        for i in range(len(answers)):
            if answers[i] == elem[i%len(elem)]:
                result[arr.index(elem)] += 1
                
    return [idx+1 for idx in range(len(result)) if result[idx] == max(result)]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))