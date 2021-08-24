import sys
from collections import deque

input = sys.stdin.readline

gear = {}
for i in range(1, 5):
    gear[i] = deque(list(map(int, input().replace("\n", ""))))

count = int(input())
def rotate(dir):
    if dir == 1:
        out = gear[gear_num].pop()
        gear[gear_num].appendleft(out)
    else:
        out = gear[gear_num].popleft()
        gear[gear_num].append(out)

def check_right(start, dir):
    if start > 4 or gear[start - 1][2] == gear[start][6]:
        return

    if gear[start - 1][2] != gear[start][6]:
        check_right(start + 1, -dir)
        rotate(dir)


def check_left(start, dir):
    if start < 1 or gear[start][2] == gear[start + 1][6]:
        return
    if gear[start + 1][6] != gear[start][2]:
        check_left(start - 1, -dir)
        rotate(dir)


for _ in range(count):
    gear_num, dir = map(int, input().split())

    check_right(gear_num + 1, -dir)
    check_left(gear_num - 1, -dir)
    rotate(dir)

res = 0
expon = 1
for i in range(1, 5):
    res += gear[i][0] * expon
    expon*=2

print(res)
