import sys
import heapq

input = sys.stdin.readline

times = []
queue = []
N = int(input())
for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(times, (start, end))
times.sort()
for time in times:
    if len(queue) == 0:
        heapq.heappush(queue,time[1])
    else:
        if queue[0] <= time[0]:
            heapq.heappop(queue)
            heapq.heappush(queue,time[1])
        else:
            heapq.heappush(queue, time[1])

print(len(queue))
