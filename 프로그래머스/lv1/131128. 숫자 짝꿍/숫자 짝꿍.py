from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    
    answer = ''
    
    # 0 ~ 9
    for i in range(10):
        answer += str(i) * min(x[str(i)], y[str(i)])
    
    if answer == '':
        return '-1'
    
    answer = answer[::-1]
    if answer[0] == '0':
        return '0'
            
    return answer