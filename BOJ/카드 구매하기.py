import sys

input = sys.stdin.readline
N = int(input())
pack = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1]=pack[1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = (max(dp[i - j] + pack[j], dp[i]))

print(dp[N])
