# 단어 정렬
N = int(input())
lst = []

for _ in range(N):
    a = input()
    if a not in lst:
        lst.append(a)

new_list = sorted(lst, key=lambda x:(len(x), x))

for i in new_list:
    print(i)