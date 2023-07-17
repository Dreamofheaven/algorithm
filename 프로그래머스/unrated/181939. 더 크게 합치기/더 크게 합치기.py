def solution(a, b):
    ans1 = str(a) + str(b)
    ans2 = str(b) + str(a)
    
    if ans1 >= ans2:
        answer = int(ans1)
    else:
        answer = int(ans2)
        
    return answer