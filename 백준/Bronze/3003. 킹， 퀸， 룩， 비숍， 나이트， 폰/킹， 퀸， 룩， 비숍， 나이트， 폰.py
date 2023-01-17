chess_list = [1, 1, 2, 2, 2, 8]
user_list = list(map(int, input().split()))

for i in range(6):
    print(chess_list[i] - user_list[i], end = " ")