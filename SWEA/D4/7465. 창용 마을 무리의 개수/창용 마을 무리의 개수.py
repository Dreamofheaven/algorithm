# 창용 마을 무리의 개수 

# 창용 마을에는 N명의 사람이 살고 있다. 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수도 있고, 아닐 수도 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다. 
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하여라. 

T = int(input())

for t in range(T):
    N, M = map(int, input().split()) # 6 5 
    persons = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        v1, v2 = map(int, input().split()) # 1 2
        persons[v1].append(v2)
        persons[v2].append(v1)

    main_visited = [False] * (N + 1)
    
    re = []

    for j in range(1, N+1):
        visited = [False] * (N + 1)
        stack = [j]
        ans = []

        while stack:
            cur = stack.pop()
            for i in persons[cur]:
                if not visited[i]:
                    visited[i] = True
                    main_visited[i] = True
                    stack.append(i)
            for k in range(N+1):
                if visited[k] == True:
                    ans.append(k)
        re.append(set(ans))

    new_result = []

    for x in re:
        if x == set():
            new_result.append(x)
        elif x not in new_result:
            new_result.append(x)
    print(f'#{t+1} {len(new_result)}')






    




