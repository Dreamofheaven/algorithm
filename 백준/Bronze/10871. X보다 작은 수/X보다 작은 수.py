# x보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))
new_list = []

for i in A:
    if i < X:
        new_list.append(i)
print(*new_list)