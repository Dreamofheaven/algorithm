# [입력] 입력으로 P와 K가 빈 칸을 사이로 주어진다. 비번은 000부터 999까지
# [출력] 몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.

P, K = map(int, input().split())
num = 1

while(P != K):
    K += 1
    num += 1
print(num)