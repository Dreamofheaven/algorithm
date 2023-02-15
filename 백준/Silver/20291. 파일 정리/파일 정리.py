# 파일정리
import sys

N = int(input())
ans_dict = {}

for _ in range(N):
    S = sys.stdin.readline()
    i = S.strip().split('.')
    
    if i[1] in ans_dict:
        ans_dict[i[1]] += 1
    else:
        ans_dict[i[1]] = 1

result = sorted(ans_dict.items())

for k in result:
    print(*k)



