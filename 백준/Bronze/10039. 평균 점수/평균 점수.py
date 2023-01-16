# 평균 구하기
scores_sum = 0
scores_average = 0

for i in range(5):
    score = int(input())

    if score < 40:
        score = 40
        scores_sum += score
    else:
        scores_sum += score
    
scores_average = int(scores_sum / 5)
print(scores_average)
    