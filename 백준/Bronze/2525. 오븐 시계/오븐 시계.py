H, M = map(int, input().split())
running_time = int(input())

if M + running_time >= 60:
    H += (M + running_time) // 60
    M = (M + running_time) % 60 
    if H >= 24:
        H -= 24 
    print(H, M)
else:
    print(H, M + running_time)
