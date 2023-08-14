N = int(input())

res = 0

for i in range(1, N+1):
    num_list = list(map(int, str(i))) 

    if i < 100:
        res += 1
    elif (num_list[0] - num_list[1]) == (num_list[1] - num_list[2]):
        res += 1
print(res)