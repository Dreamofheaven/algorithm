# 백준 명령 프롬프트 

N = int(input())
target =  list(input())
result = ""

for i in range(N-1):
    s = list(input())
    for j in range(len(target)):
        if target[j] != s[j]:
            target[j] = "?"
print(''.join(target))
    




