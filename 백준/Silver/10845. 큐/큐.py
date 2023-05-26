import sys

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    method_list = sys.stdin.readline().split()

    if len(method_list) == 2:
        queue.append(method_list[-1])
    elif method_list[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif method_list[0] == "size":
        print(len(queue))
    elif method_list[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif method_list[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif method_list[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])