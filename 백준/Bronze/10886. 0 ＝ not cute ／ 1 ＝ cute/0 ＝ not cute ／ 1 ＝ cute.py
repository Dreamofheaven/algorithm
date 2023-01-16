# 0 = not cute / 1 = cute
N = int(input()) # 설문조사 인원, 홀수

not_cute_vote_result = 0
cute_vote_result = 0

for i in range(N):
    vote = int(input())
    if vote == 0:
        not_cute_vote_result += 1
    else:
        cute_vote_result += 1
if not_cute_vote_result > cute_vote_result:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
