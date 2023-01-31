# 누울 자리를 찾아라
N = int(input())

matrix = [input() for _ in range(N)]
row_cnt = 0
column_cnt = 0

# 행 기준 (가로)
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row_cnt += 1
         
# 열 기준 (세로)
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            column_cnt += 1

print(row_cnt, column_cnt)
