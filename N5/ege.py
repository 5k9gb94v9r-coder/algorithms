INF = 10 ** 9

n, m, k, c = map(int, input().split())
cities = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, t))
    graph[v].append((u, t))

used = [False] * n
dist = [INF] * n
dist[c - 1] = 0

for i in range(n):
    min_idx = -1
    for j in range(n):
        if used[j]:
            continue
        if min_idx == -1 or dist[min_idx] > dist[j]:
            min_idx = j

    if dist[min_idx] == INF:
        break

    used[min_idx] = True

    for u, w in graph[min_idx]:
        if used[u]:
            continue
        if dist[u] > dist[min_idx] + w:
            dist[u] = dist[min_idx] + w

result = []
for city in cities:
    result.append((dist[city - 1], city))

result.sort()

for time, city in result:
    print(city, time)