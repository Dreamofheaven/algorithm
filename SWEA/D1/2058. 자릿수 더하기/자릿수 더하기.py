N = int(input())
result = 0

while (N > 10):
    result += (N % 10)
    N = N // 10
result += N
print(result)