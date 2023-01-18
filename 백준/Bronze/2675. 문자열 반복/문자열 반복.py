T = int(input())

for t in range(1, T+1):
    n_word = ''
    R, S = map(str, input().split())

    for i in S:
        n_word += i * int(R)
        
    print(n_word)