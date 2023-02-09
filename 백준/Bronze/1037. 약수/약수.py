# 백준 약수 

N = int(input())

divisor_list = list(map(int, input().split()))

if N == 1:
    print(divisor_list[0] * divisor_list[0])
else:
    print(min(divisor_list) * max(divisor_list))