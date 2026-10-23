INF = 10**9
n, m = map(int, input().split())

dist = [[INF]* n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w < dist[u][v]:
        dist[u][v] = w
        dist[v][u] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

best_vertex = -1
best_max_dist = INF

for i in range(n):
    max_dist = max(dist[i])

    if max_dist < best_max_dist:
        best_max_dist = max_dist
        best_vertex = i + 1

print(best_vertex)