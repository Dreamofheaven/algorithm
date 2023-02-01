# 점수 집계

T = int(input())

for t in range(T):
    scores = list(map(int, input().split()))
    sorted_scores = sorted(scores, reverse=True)

    new_scores = sorted_scores[1:-1]
    if new_scores[0] - new_scores[-1] >= 4:
        print("KIN")
    else:
        print(sum(new_scores))

  

