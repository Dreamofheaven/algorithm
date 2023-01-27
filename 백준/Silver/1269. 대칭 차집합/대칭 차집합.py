len_A, len_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

new = A ^ B
print(len(new))