# 지능형 기차
# 내린사람 / 탄 사람

total = 0
stack = []

for _ in range(4):
    out_n, in_n = map(int, input().split())

    total = total - out_n + in_n
    stack.append(total)

print(max(stack))




