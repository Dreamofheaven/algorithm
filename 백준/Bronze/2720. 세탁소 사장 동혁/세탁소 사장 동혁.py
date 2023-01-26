# 세탁소 사장 동혁

T = int(input())

# 쿼터, 다임, 니켈, 페니

for t in range(T):
    change = int(input())
    for i in [25, 10, 5, 1]:
        print((change // i), end = ' ')
        change %= i