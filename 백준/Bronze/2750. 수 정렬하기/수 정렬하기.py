N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(input()))
numbers = sorted(numbers)

for j in numbers:
    print(j)