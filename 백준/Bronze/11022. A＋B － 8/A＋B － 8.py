T = int(input()) # 테스트케이스 수

for x in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{x}: {A} + {B} = {A + B}') 