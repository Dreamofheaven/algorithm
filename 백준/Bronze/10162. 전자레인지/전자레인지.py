T = int(input())

time = [5 * 60, 1 * 60, 10]
res = {time[0] : 0, time[1] : 0, time[2] : 0}

for t in time:
    if t <= T:
        tmp = T // t
        res[t] += tmp
        T %= t
    else:
        res[t] = 0

if T == 0:
    print(*res.values())
else:
    print(-1)