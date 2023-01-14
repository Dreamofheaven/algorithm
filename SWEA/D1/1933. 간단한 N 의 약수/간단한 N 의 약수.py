N = int(input())

divisor_list = [1]

for i in range(2, N+1):
    if N % i == 0:
        divisor_list.append(i)
print(*divisor_list)