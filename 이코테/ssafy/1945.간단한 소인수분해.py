T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a, b, c, d, e = [0, 0, 0, 0, 0]
    while n >= 2:
        if n % 11 == 0:
            n //= 11
            e += 1
        if n % 7 == 0:
            n //= 7
            d += 1
        if n % 5 == 0:
            n //= 5
            c += 1
        if n % 3 == 0:
            n //= 3
            b += 1
        if n % 2 == 0:
            n //= 2
            a += 1
    print(f'#{test_case} {a} {b} {c} {d} {e}')

