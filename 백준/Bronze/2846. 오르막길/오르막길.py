#오르막길

N = int(input())
numbers = list(map(int, input().split()))
n = 0
upper_list = []

for i in range(N-1):
    if numbers[i] < numbers[i+1]:
        n += numbers[i+1] - numbers[i]
    else:
        upper_list.append(n)
        n = 0
upper_list.append(n)
print(max(upper_list))
        