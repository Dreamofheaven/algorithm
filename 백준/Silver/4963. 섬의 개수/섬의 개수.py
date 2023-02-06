# 섬의 개수

d = [(1,1),(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
stack = []

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                stack.append((i, j))
                # 방문했다는 표시로 값을 0으로 바꿔준다.
                island[i][j] = 0
                cnt += 1

                while stack:
                    # 현재 위치를 q에서 꺼내준다.
                    cx, cy = stack.pop()
                    for a, b in d:
                        dx = cx + a
                        dy = cy + b
                        if h > dx >= 0 and w > dy >= 0 and island[dx][dy]:
                            stack.append((dx, dy))
                            island[dx][dy] = 0
    print(cnt)



    




    