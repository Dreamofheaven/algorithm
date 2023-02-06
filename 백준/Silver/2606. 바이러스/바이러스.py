# 바이러스

C = int(input())
N = int(input())

graph = [[] for _ in range(C + 1)]

for _ in range(N):
    v1, v2 = map(int, input().split()) # 1 2
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (C + 1)
stack = [1]
visited[1] = True

while stack:
    cur = stack.pop()

    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)
    
print(visited.count(True) - 1)
