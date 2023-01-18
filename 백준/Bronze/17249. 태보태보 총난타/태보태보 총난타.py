S = input()
new_S = S.split('0')

left_cnt = new_S[0].count('@')
right_cnt = new_S[1].count('@')

print(left_cnt, right_cnt)