k =  int(input())
stack_list = []

for i in range(k):
    n = int(input())
    if n != 0:
        stack_list.append(n)
    else:
        stack_list.pop()
print(sum(stack_list))