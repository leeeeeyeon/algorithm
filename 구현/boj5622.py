import sys

input = sys.stdin.readline

word = list(input())
word.pop()

def wordToNum(a):
    if a == 'A' or a == 'B' or a == 'C':
        return 2
    if a == 'D' or a == 'E' or a == 'F':
        return 3
    if a == 'G' or a == 'H' or a == 'I':
        return 4
    if a == 'J' or a == 'K' or a == 'L':
        return 5
    if a == 'M' or a == 'N' or a == 'O':
        return 6
    if a == 'P' or a == 'Q' or a == 'R' or a == 'S':
        return 7
    if a == 'T' or a == 'U' or a == 'V':
        return 8
    if a == 'W' or a == 'X' or a == 'Y' or a == 'Z':
        return 9

num = list(map(wordToNum, word))
print(sum(num)+len(num))

# 다른 사람 코드
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)

# 피드백
# 알파벳 4개 있는 곳이 WXYZ 말고 다른 곳에도 있다 ...!