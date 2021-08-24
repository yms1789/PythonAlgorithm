import sys

input = sys.stdin.readline
N, M = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

dp = [0] * (M + 1)
dp[0] = 1
for i in range(N):
    for j in range(coin[i], M + 1):
        if j - coin[i] >= 0:
            dp[j] += dp[j - coin[i]]
print(dp[M])
