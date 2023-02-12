def solution(lotteries):
    answer = 0

    mx = []
    for i in range(len(lotteries)):
        lottery = lotteries[i]
        a, b, c = lottery[0], lottery[1], lottery[2] # 당첨자 수, 구매한 사람 수, 당첨 금액
        percent = (a/(b+1)) * 100
        if percent > 100:
            percent = 100
        mx.append([i+1, percent, c]) # 번호, 확률, 당첨 금액

    mx.sort(key = lambda x: (-x[1], -x[2]))
    return mx[0][0]

print(solution([[100, 100, 500],[1000, 1000, 100]]))
print(solution([[10, 19, 800],[20, 39, 200], [100, 199, 500]]))
print(solution([[50, 1, 50],[100, 199, 100], [1, 1, 500]]))
    