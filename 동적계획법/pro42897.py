def solution(money):
    zero = [0 for _ in range(len(money)-1)]
    one = [0 for _ in range(len(money)-1)]
    
    zero[0] = money[0]
    zero[1] = max(money[0], money[1])
    
    one[0] = money[1]
    one[1] = max(money[1], money[2])
    
    for i in range(2, len(zero)):
        zero[i] = max(zero[i-2]+money[i], zero[i-1])
    
    for i in range(2, len(one)):
        one[i] = max(one[i-2]+money[i+1], one[i-1])
    

    return max(zero[-1], one[-1])