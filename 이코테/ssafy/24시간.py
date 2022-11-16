T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    if n + m < 24:
        print(f'{test_case} {n + m}')
    else:
        print(f'{test_case} {n + m - 24}')

