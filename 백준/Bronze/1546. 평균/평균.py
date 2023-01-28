N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_sum = 0

for i in scores:
    new_sum += (i / max_score * 100)

print(new_sum / N)