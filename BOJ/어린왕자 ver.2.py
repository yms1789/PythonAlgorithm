import sys
from math import sqrt
from math import pow

input = sys.stdin.readline

test = int(input())
for _ in range(test):
    cnt = 0
    start_x, start_y, end_x, end_y = map(int, input().split())
    circle_num = int(input())
    for i in range(circle_num):
        cir_x, cir_y, rad = map(int, input().split())
        distance_start = sqrt(pow((start_x - cir_x),2) + pow((start_y - cir_y),2))
        distance_end = sqrt(pow((end_x - cir_x),2) + pow((end_y - cir_y),2))
        if (distance_start < rad) ^ (distance_end < rad):
            cnt += 1
    print(cnt)
