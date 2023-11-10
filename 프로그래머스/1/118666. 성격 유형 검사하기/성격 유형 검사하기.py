def solution(survey, choices):
    res = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }

    matched_list = list(zip(survey, choices))
    answer = ''

    for i in matched_list:
        score = i[1] - 4
        if score < 0:
            res[i[0][0]] += abs(score)
        else:
            res[i[0][1]] += score

    res_list = list(res.items())

    for j in range(0, len(res_list), 2):
        # 두번째 것이 더 크면 뒤어꺼를 ans에 더하고
        # 첫번째 것이 더 크거나 같으면 ans에 앞의 것을 더해야해서
        if res_list[j][1] < res_list[j+1][1]:
            answer += res_list[j+1][0]
        else:
            answer += res_list[j][0]    
    
    return answer
