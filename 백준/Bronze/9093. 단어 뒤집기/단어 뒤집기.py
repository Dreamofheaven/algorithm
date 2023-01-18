T = int(input())

for t in range(T):
    new_S = ""
    S = list(map(str, input().split()))
    
    for i in S:
        new_S += i[::-1]
        new_S += " "
    print(new_S)
