N = int(input())
numbers = list(map(int, input().split()))
new_list = [] 
cnt = 0

for i in range(N):
    if numbers[i] not in new_list:
        new_list.append(numbers[i])
    else:
        cnt += 1
print(cnt)