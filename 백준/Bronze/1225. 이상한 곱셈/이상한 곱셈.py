# 이상한 곱셈
A, B = input().split()
list_A = list(map(int, A))
list_B = list(map(int, B))
# for i in A:
#     for j in B:
#         result += int(i)*int(j)
# print(result)
print(sum(list_A) * sum(list_B))