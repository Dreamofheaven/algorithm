# 공 

M = int(input())
cup = [1, 0, 0]

for _ in range(M):
    a, b = map(int, input().split())
    cup[b-1], cup[a-1] = cup[a-1], cup[b-1]
print(cup.index(1)+1)

