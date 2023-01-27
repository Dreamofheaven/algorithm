# 절댓값 힙
import heapq, sys
heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    i = int(sys.stdin.readline())

    if i != 0:
        heapq.heappush(heap, (abs(i), i))
    elif i == 0 and len(heap) == 0:
        print(0)
    elif i ==0:
        print(heapq.heappop(heap)[1])