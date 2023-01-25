X = int(input()) # 총 금액
N = int(input()) # 구매한 물건의 개수 
result = 0

for i in range(N):
    a, b = map(int, input().split())
    result += (a * b)

if X ==  result:
    print('Yes')
else:
    print('No')