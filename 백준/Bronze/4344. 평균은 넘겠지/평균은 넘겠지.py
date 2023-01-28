C = int(input())

for c in range(C):
    a = list(map(int, input().split()))
    average = (sum(a[1:]) // a[0])

    cnt = 0
    for i in a[1:]:
        if i > average:
            cnt += 1
    print(f'{(cnt / a[0] * 100):.3f}%')
