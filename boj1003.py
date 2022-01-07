t = int(input())

for _ in range(0,t):
    n = int(input())
    zero = [0] * (n+2)
    one = [0] * (n+2)
    for i in range(0, n+1):
        if i == 0:
            zero[i] = 1
        elif i == 1:
            one[i] = 1
        else:
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
    print(zero[n], one[n])