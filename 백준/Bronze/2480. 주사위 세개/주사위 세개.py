dice = list(map(int, input().split()))
new_list = []
same_dice = 0

for i in dice:
    if i in new_list:
        same_dice = i
    else:
        new_list.append(i)

if len(new_list) == 2:
    print(1000 + same_dice * 100)
elif len(new_list) == 1:
    print(10000 + same_dice * 1000)
else:
    print(max(new_list) * 100)