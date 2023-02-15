# 파일정리

N = int(input())

ans = []
ans_dict = {}

for _ in range(N):
    S = input()
    i = S.index('.')

    ans.append(S[i+1:])

for j in ans:
    if j in ans_dict:
        ans_dict[j] += 1
    else:
        ans_dict[j] = 1

result = sorted(ans_dict.items())

for k in result:
    print(*k)



