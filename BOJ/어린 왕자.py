import sys

input = sys.stdin.readline

# 해당 원의 모든 좌표를 리스트에 저장
def inside_circle(circle_info):
    for i in range(len(circle_info)):
        c_x, c_y, r = circle_info.pop()
        for add in range(r):
            dx = [add, -add, 0, 0]
            dy = [0, 0, add, -add]
            for j in range(4):
                c_nx, c_ny = c_x + dx[j], c_y + dy[j]
                if [c_nx, c_ny] in circle_all_ㅣoc:
                    continue
                circle_all_ㅣoc[i].append([c_nx, c_ny])
    return circle_all_ㅣoc


res_arr = []
test = int(input())
for i in range(test):
    start_x, start_y, end_x, end_y = map(int, input().split())
    circle_num = int(input())
    cnt = 0
    circle_info = []
    for j in range(circle_num):
        cir_x, cir_y, rad = map(int, input().split())
        circle_all_ㅣoc = [[] for i in range(circle_num)]
        circle_info.append((cir_x, cir_y, rad))
    inside_circle(circle_info)
    for circle in range(circle_num):
        if [start_x, start_y] in circle_all_ㅣoc[circle]:
            if [end_x, end_y] in circle_all_ㅣoc[circle]:
                continue
            cnt += 1
        if [start_x, start_y] not in circle_all_ㅣoc[circle]:
            if [end_x, end_y] in circle_all_ㅣoc[circle]:
                cnt += 1

    res_arr.append(cnt)

for num in range(test):
    print(res_arr[num])
