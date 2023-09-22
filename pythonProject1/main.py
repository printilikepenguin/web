from heapq import heappop, heappush
def dijkstra(start):
    pq = []
    distance[0] = 0
    heappush(pq, (start, 0))

    while pq:
        dist, node = heappop(pq)
        for next_dist, next_node in graph[node]:
            total_dist = dist + next_dist
            if distance[next_node] > total_dist:
                distance[next_node] = total_dist
                heappush(pq, (total_dist, next_node))

N, M, K = map(int, input().split())
distance = [float('inf')] * (N+1)
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
A, B = map(int, input().split())
for _ in range(B):
    s, e, w = map(int, input().split())
    graph[s] = graph.append([e, w])
for i in range(K):
    cost = map(int, input().split())