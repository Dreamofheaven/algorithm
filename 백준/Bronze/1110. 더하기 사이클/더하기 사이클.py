N = int(input()) #26
target_N = N #26
cnt = 0

while(True):
    num = (N // 10) + (N % 10) 
    N = int(str(N % 10) + str(num % 10))
    cnt += 1

    if N == target_N:
        print(cnt)
        break