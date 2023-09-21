import heapq

def dijkstra():
    pq = []
    distance[0] = 0  # 시작노드 초기화
    heapq.heappush(pq, (0, 0))  # (비용, 노드)

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            total = dist + next_dist
            if distance[next_node] > total:
                distance[next_node] = total
                heapq.heappush(pq, (distance[next_node], next_node))

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    distance = [float('inf')] * V
    visited = [False] * V

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra()

    print(f'#{tc} {distance[V - 1]}')
