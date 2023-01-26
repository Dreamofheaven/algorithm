T = int(input())

for i in range(T):
    stack = []
    ps = input()

    for k in ps:
        if k == '(':
            stack.append(k)
        elif k == ')':
            if len(stack) == 0:
                stack.append(k)
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')