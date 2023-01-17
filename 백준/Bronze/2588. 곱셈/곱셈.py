X = int(input()) # 세자리 수
Y = int(input()) # 세자리 수

a = X * (Y % 10)
b = X * ((Y // 10) % 10)
c = X * (Y // 100)

print(a)
print(b)
print(c)
print(a + 10*b + 100*c)