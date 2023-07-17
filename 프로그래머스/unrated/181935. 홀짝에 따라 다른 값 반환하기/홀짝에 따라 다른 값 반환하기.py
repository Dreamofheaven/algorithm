def solution(n):
    answer = 0
    if n % 2 == 0:
        ans1 = list(range(1, n+1))
        for i in ans1:
            if i % 2 == 0:
                answer += (i**2)
    else:
        ans2 = list(range(1, n+1))
        for i in ans2:
            if i % 2 != 0:
                answer += i
                
    return answer