import sys

input = sys.stdin.readline

string = input()
n, m = string.split(':')
m = m.rstrip('\n')


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


div = gcd(int(n), int(m))
print(int(n) // div, end='')
print(':', end='')
print(int(m) // div)
