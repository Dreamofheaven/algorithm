S = input()
croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

for i in croatia_alpabet:
    S = S.replace(i, 'o')
print(len(S))
