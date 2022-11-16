T = 10
for test_case in range(1, T + 1):
    TC = int(input())
    N, M = map(int, input().split())
    print(N, M)
    print(f'#{TC} {N ** M}')
