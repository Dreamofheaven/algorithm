a = int(input())
b = int(input())
c = int(input())
tri_list = [a, b, c]

if a == b == c == 60:
    print('Equilateral')
elif sum(tri_list) == 180:
    if len(set(tri_list)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error') 