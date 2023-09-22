# 알뜰 기차 여행
# distance 최단거리 테이블
import heapq

V, E = map(int, input().split())
graph = [[] for i in range(V)]
distance = [float('inf')] * V  # 최단거리 테이블을 모두 초기화(리스트받아서 개수처리)
visited = [False] * V
pq = []  # 우선순위 큐

for _ in range(E):
    from_node, to, cost = map(int, input().split())
    graph[from_node].append((to, cost))


def dijkstra(node):
    distance[0] = 0  # 시작노드 초기화
    heapq.heappush(pq, (0, 0))  # (비용, 노드)

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)  # 우선순위 큐에서 현재노드/비용 가져옴
        if visited[cur_node]:  # 이미 방문한 노드라면
            continue
        visited[cur_node] = True  # 방문처리
        # 현재 노드와 연결된 다른 노드를 확인
        for next_node, edge_cost in graph[cur_node]:
            total_cost = cur_cost + edge_cost  # 총비용 계산
            if distance[next_node] > total_cost:  # 최단거리 테이블 갱신 조건 확인
                distance[next_node] = total_cost
                heapq.heappush(pq, (distance[next_node], next_node))  # 우선순위 큐에 새로운 노드 정보 추가

dijkstra()
if distance[V-1] == float('inf'):
    print('impossible')
else:  # 도착지점에 도달하는 비용 출력
    print(distance[V-1])