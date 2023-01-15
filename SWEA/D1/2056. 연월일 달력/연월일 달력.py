
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input() # 8자리 숫자
    
    year = N[0:4]
    month = N[4:6]
    day = N[6:8]
    # print(year, month, day)
    ok_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    if int(year) > 0 and 0 < int(month) < 13 and int(day) <= ok_dict[int(month)]:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} {-1}')

