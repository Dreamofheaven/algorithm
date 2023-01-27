# 고무오리 디버깅
stack = []

while(True):
    a = input()
       
    if a == "문제":
        stack.append(a)
    elif a == "고무오리":
        if len(stack) != 0:
            stack.pop()
        else:
            stack.append("문제")
            stack.append("문제")
    elif a == "고무오리 디버깅 끝":
        break

if len(stack) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")