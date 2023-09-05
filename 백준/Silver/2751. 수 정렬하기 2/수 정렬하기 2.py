import sys

input = sys.stdin.readline

N = int(input())
res_list = []

for _ in range(N):
    n = int(input())
    res_list.append(n)

res_list.sort()

for i in res_list:
    print(i)