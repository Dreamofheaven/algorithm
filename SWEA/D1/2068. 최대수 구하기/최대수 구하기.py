
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    numbers = list(map(int,input().split()))
    print(f'#{t} {max(numbers)}')