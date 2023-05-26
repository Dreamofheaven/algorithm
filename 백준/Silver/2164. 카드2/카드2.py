from collections import deque
import sys

N = int(sys.stdin.readline())
a = deque(range(1, N+1)) # 1부터 N까지의 카드 

while (len(a) > 1):
    a.popleft()
    a.append(a.popleft())
print(a[0])