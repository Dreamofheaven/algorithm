def solution(str1, str2):
    str3 = list(zip(str1, str2))
    answer = ''
    
    for x in str3:
        answer += x[0]
        answer += x[1]
    return answer