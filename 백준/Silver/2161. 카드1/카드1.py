N = int(input())
a = list(range(1, N+1))

while(len(a) > 1):
    print(a.pop(0), end=" ")
    a.append(a.pop(0))
print(*a)