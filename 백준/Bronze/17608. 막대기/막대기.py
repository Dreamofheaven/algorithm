# 막대기
import sys

N = int(input()) # 막대의 개수
stack = []
visible_var, cnt = 0, 0

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

while stack:
    tmp = stack.pop()
    if visible_var < tmp:
        visible_var = tmp
        cnt += 1
    
print(cnt)
    