# 블랙잭

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
max_total = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = numbers[i] +  numbers[j] + numbers[k]

            if max_total < total <= M:
                max_total = total
            if total == M:
                max_total = total
                break
print(max_total)
