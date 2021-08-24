import sys

input = sys.stdin.readline
N = int(input())
road = [[0] * 3 for _ in range(N)]
cost = []
for _ in range(N):
    RGB = list(map(int, input().split()))
    cost.append(RGB)

for i in range(N):
    if i == 0:
        road[i][0] = cost[i][0]
        road[i][1] = cost[i][1]
        road[i][2] = cost[i][2]

    #R
    road[i][0] = min(road[i - 1][1], road[i - 1][2]) + cost[i][0]
    #G
    road[i][1] = min(road[i - 1][0], road[i - 1][2]) + cost[i][1]
    #B
    road[i][2] = min(road[i - 1][0], road[i - 1][1]) + cost[i][2]

    min_cost = min(min(road[N-1][0],road[N-1][1]),road[N-1][2])

print (min_cost)