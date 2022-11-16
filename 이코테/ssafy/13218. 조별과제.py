T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    count = 0
    while n >= 3:
        n -= 3
        count += 1
    print(f'#{test_case} {count}')
