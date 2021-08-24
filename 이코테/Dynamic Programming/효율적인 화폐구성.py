import sys

input = sys.stdin.readline

N, M = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

dp = [10001] * (M + 1)

dp[0] = 0

for i in range(N):
    for j in range(coin[i], M + 1):
        if dp[j - coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
