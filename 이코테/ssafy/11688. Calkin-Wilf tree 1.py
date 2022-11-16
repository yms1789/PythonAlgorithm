from fractions import Fraction

T = int(input())
for test_case in range(1, T + 1):
    left_right = input()
    num = Fraction(1, 1)

    for ele in left_right:
        if ele == 'R':
            num = Fraction(num.numerator + num.denominator, num.denominator)
        elif ele == 'L':
            num = Fraction(num.numerator, num.numerator + num.denominator)
    if left_right[-1] == 'R':
        print(f'#{test_case} {num.numerator} {num.denominator}')
    elif left_right[-1] == 'L':
        print(f'#{test_case} {num.numerator} {num.denominator}')
