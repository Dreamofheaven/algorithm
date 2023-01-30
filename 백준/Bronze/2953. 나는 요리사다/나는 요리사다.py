matrix = [list(map(int, input().split())) for _ in range(5)]
dict = {}

for i in matrix:
    dict[matrix.index(i) + 1] = sum(i)
result_index = max(dict, key=dict.get)
print(result_index, dict[result_index])
