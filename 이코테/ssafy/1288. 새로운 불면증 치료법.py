T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    zero_to_nine = list(map(int, str(N)))
    mul = 2
    count = 1
    while len(zero_to_nine) != 10:
        next_N = list(map(int, str(mul * N)))
        count = mul * N
        mul += 1
        zero_to_nine += next_N
        zero_to_nine = list(set(zero_to_nine))
    print(f'#{test_case} {count}')
