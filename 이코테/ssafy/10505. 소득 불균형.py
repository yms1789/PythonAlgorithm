T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    m = list(map(int, input().split()))
    income_avg = sum(m) // n
    count = 0
    for income in m:
        if income <= income_avg:
            count += 1
    print(f'#{test_case} {count}')
