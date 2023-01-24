import sys

input = sys.stdin.readline

n = int(input())
queen_col = [0 for _ in range(n)]
count = 0

def promising(row):
    for i in range(row):
        if queen_col[row] == queen_col[i] or abs(queen_col[row] - queen_col[i]) == row - i:
            return False
    return True

def nqueen(row):
    if row == n:
        global count
        count += 1
        return
    
    for col in range(n):
        queen_col[row] = col

        if promising(row):
            nqueen(row+1)

nqueen(0)
print(count)      