# 이상한 곱셈
A, B = map(str, input().split())
result = 0

for i in A:
    for j in B:
        result += int(i)*int(j)
print(result)
    