# 덩치
N = int(input())
info = []

for _ in range(N):
    x, y = map(int, input().split())
    info.append((x, y))

result = [1] * N # 덩치 큰 거 카운트

for i in range(N-1):
    for j in range(i+1, N):
        # 몸무게 비교하기 index = 0, 키 비교하기 index = 1
        if (info[i][0] > info[j][0]) and (info[i][1] > info[j][1]):
            result[j] += 1
        elif (info[i][0] < info[j][0]) and (info[i][1] < info[j][1]):
            result[i] += 1
print(*result)
    
        