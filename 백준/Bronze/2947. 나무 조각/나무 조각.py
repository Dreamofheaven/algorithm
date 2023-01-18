numbers = list(map(int, input().split()))
tmp = 0

while(True):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            tmp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = tmp
            print(*numbers)
    if numbers == [1, 2, 3, 4, 5]:
        break
