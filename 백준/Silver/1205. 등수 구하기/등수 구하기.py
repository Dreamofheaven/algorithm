N, newScore, P = map(int, input().split())

if N <= 0:
    print(1)
else:
    score = list(map(int, input().split()))
    score.append(newScore)
    score.sort(reverse=True)
    idx = score.index(newScore) + 1

    if idx > P: 
        print(-1)
    else:
        if N == P and newScore == score[-1]:
            print(-1)
        else:
            print(idx)