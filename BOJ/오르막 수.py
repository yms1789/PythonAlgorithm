import sys

input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        if j < 1:
            dp[i][j] = 1
        elif i >= 2 or j >= 1:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
sum = 0
for i in range(10):
    sum += dp[N][i]
print(sum%10007)
