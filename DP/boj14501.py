# 내 코드
n = int(input())

t = [0] * (n + 2)
p = [0] * (n + 2)
dp = [0] * (n + 2) # 0 ~ n + 1

# t, p 입력 받음
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1): # 7 6 5 4 3 2 1
    if n - i + 1 - t[i] < 0:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(p[i] + dp[i+t[i]], dp[i+1])

print(dp[1])

# 다른 사람 코드
# #include <iostream>
 
# using namespace std;
 
# int t[1000] = { 0, };
# int p[1000] = { 0, };
# int dp[1000] = { 0, };
 
# int max(int x, int y)
# {
#     return x > y ? x : y;
# }
 
# int main()
# {
#     int N;
#     int next;
 
#     cin >> N;
 
#     for (int i = 1;i <= N;i++) {
#         cin >> t[i] >> p[i];
#     }
 
#     for (int i = N;i > 0;i--) {
#         next = i + t[i];
#         if (next > N + 1) {
#             dp[i] = dp[i + 1];
#         }
#         else {
#             dp[i] = max(dp[i + 1], dp[next] + p[i]);
#         }
 
#     }
 
#     cout << dp[1] << endl;
 
#     return 0;
# }

# 피드백
# - 참고: https://songsunbi.tistory.com/80
# - 마지막 > 첫째 날 순으로 생각하면 더 쉽다.
