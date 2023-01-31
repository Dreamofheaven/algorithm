# 박스 

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]

    result_sum = 0
    for j in range(n):
        result = 0
        cnt = 0
        for i in range(m-1, -1, -1):
            if matrix[i][j] == 0:
                cnt += 1
            else:
                result += cnt
        result_sum += result
    print(result_sum)

