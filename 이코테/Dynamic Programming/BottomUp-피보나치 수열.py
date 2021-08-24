# 다이나믹프로그래밍의 전형적인 형태는 BottomUp 방식 - 일반적으로 반복문을 사용하여 구현함.
# 결과 저장용 리스트는 DP 테이블이라고 부름.

dp = [0] * 100

dp[1] = 1
dp[2] = 1
N = 99

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
