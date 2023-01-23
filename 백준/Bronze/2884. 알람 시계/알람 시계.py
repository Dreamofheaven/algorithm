H, M = map(int, input().split())

if H == 0:
    alram = (24 * 60 + M) - 45
    new_H = alram // 60
    if new_H == 24:
        print(0, alram % 60)
    else:
        print(new_H, alram % 60)
else:
    alram = (H * 60 + M) - 45
    print(alram // 60, alram % 60)