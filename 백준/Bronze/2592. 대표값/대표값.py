# 대표값
numbers = [int(input()) for _ in range(10)]
result_dict = {}


for i in numbers:
    if i in result_dict:
        result_dict[i] += 1
    else:
        result_dict[i] = 1

average_num = sum(numbers) // 10
mode_num = max(result_dict, key=result_dict.get)

print(average_num, mode_num)

