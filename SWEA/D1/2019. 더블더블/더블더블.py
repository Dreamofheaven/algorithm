T = int(input())
n = 1

for t in range(1, T+2):
    if t == 1:
        print(n, end=" ")
    else:
        n *= 2
        print(n, end=" ")
    
    
    