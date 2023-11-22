N = int(input())

video = []

for _ in range(N):
    video.append(input())

def quadTree(x, y ,N):
    if N == 1:
        result.append(video[x][y])
        return 
    
    stand = video[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if video[i][j] != stand:
                N //= 2
                result.append("(")
                quadTree(x,y,N)
                quadTree(x,y+N,N)
                quadTree(x+N,y,N)
                quadTree(x+N,y+N,N)
                result.append(")")
                return
    result.append(stand)
    return

result = []

quadTree(0, 0, N)
print("".join(result))