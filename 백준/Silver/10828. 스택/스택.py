# 스택 
import re, sys

N = int(sys.stdin.readline())

stack_list = []

for i in range(N):
    method_list = sys.stdin.readline().split()
    
    if len(method_list) == 2:
        stack_list.append(method_list[-1])
    elif method_list[0] == "pop":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())
    elif method_list[0] == "size":
        print(len(stack_list))
    elif method_list[0] == "empty":
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif method_list[0] == "top":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])