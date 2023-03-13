def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] <= phone_book[i+1] and phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False        
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

# 피드백
# 정렬을 했으면 i와 i+1만 비교하면 되고, i+2 이후는 비교하지 않아도 된다
# [0]이 [2]의 접두어였다면, [1]도 [2]의 접두어라는 것이 보장되기 때문이다
# 이를 통해 2중 루프를 1중 루프로 줄일 수 있다