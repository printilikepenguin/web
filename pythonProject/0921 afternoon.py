'''
DFS, BFS 공통점: 그래프나 트리의 노드들을 탐색하는 방법론
DFS는 깊이 우선, BFS는 가까운 노드(레벨)부터

Union-Find는 그래프의 노드들을 집합으로 관리
1. 두 노드가 같은 집합에 속하는지 or
2. 두 집합을 하나로 합치는 연산을 효율적으로 수행하는데 사용

Dijkstra
가중치있는 그래프에서 한 노드로부터 다른 모든 노드까지의 최단거리를 찾는다
'''
#
# # 순환회로검사
# def find_set(x):
#     if parent[x] == x:
#         return x
#     return find_set(parent[x])
#
# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)
#     if x != y:
#         parent[x] = y
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# parent = [i for i in range(N)]
#
# for i in range(N):
#     for j in range(i+1, N):
#         if arr[i][j] == 0:
#             continue
#         if find_set(i) == find_set(j):
#             print('WARNING')
#             exit()
#         # 두 노드 연결
#         union(i, j)
# print('STABLE')
#
# # 해당 노드의 최상위 노드를 찾는 함수
# def find(node):
#     if node == parent[node]:
#         return node
#     parent[node] = find(parent[node])
#     return parent[node]
#
# # 두 노드를 연결하는 함수
# def onion(a, b):
#     pa = find(a)
#     pb = find(b)
#     if pa != pb:
#         parent[pb] = pa
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# parent = [i for i in range(N)]
#
# for i in range(N):
#     for j in range(i+1, N):
#         # 두 노드가 연결되어 있지 않다면
#         if arr[i][j] == 0:
#             continue
#         # 만약 두 노드의 최상위 부모(루트)가 같다면
#         if find(i) == find(j):
#             print('WARNING')
#             exit()
#         # 두 노드 연결
#         onion(i, j)
# print('STABLE')
#
#
# '''
# # 사이클 발생 여부를 union find 로 해결
# parents = [i for i in range(V)]
#
# def find_set(x):
#     if parents[x] == x:
#         return x
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)
#
#     if x == y:
#         print('사이클 발생')
#         return
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y
#
# # 현재 방문한 정점 수
# cnt = 0
# sum_weight = 0
# for f, t, w in edge:
#     # 싸이클이 발생하지 않는다면
#     if find_set(f) != find_set(t):
#         cnt += 1
#         sum_weight += w
#         union(f, t)
#         # MST 구성이 끝나면
#         if cnt == V:
#             break
#
# '''
#
#
# # 최소신장트리 : 간선의 가중치를 모두 더한 값을 출력하시오
# def find_set(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find_set(parent[x])
#     return parent[x]
#
# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)
#     if x == y:
#         return
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     edge = []
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         edge.append([n1,n2,w])
#     # 그래프의 간선들을 가중치의 오름차순으로 정렬한다
#     edge.sort(key=lambda x: x[2])
#     # 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다
#     ## 가장 낮은 가중치 먼저 선택
#     ## 사이클 형성 간선 제외
#     # 해당 간선을 현재 MST의 집합에 추가
#     parent = [i for i in range(V+1)]
#
#     cnt = total = 0
#
#     for i in range(E):
#         if cnt == V:
#             break
#         s, e, w = edge[i]
#         if find_set(s) == find_set(e):
#             continue
#         union(s, e)
#         total += w
#     print(f'#{tc} {total}')
#
#
# # 최소 신장트리 강사님 코드
# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]
#
# def union(a, b):
#     pa = find(a)
#     pb = find(b)
#     if pa < pb:
#         parent[pb] = parent[pa]
#     else:
#         parent[pa] = parent[pb]
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     # 가중치를 기준으로 정렬
#     edges = sorted([list(map(int, input().split())) for _ in range(E)], key = lambda x: x[2])
#     parent = [i for i in range(V+1)]  # 각 노드의 초기 부모노드는 자기 자신
#     total_v = 0  # 최소 가중치의 합
#     cnt = 0
#     for i in range(E):
#         if cnt == V:  # 모든 노드가 연결되면
#             break
#         s,e,w = edges[i]
#         if find(s) == find(e):
#             continue
#         union(s,e)
#         total_v += w  # 가중치의 합 갱신
#     print(f'#{tc} {total_v}')
#

# # 최소비용
# from collections import deque
#
# def bfs(r, c):
#     dir = [(1,0), (0,1), (-1,0), (0,-1)]
#     visited[r][c] = 0  # 시작지점 연료소비량 0 초기화
#     que = deque()
#     que.append((r, c))
#     while que:
#         r, c = que.popleft()
#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
#             # 이동가능한 범위 내 있을 때
#             if 0<=nr<N and 0<=nc<N:
#                 val = 0
#                 # 현재 지점보다 높은 지역으로 이동할 때 높이차 계산
#                 if arr[nr][nc] > arr[r][c]:
#                     val = arr[nr][nc] - arr[r][c]
#                 # 이동하려는 위치와 인류 소비량 갱신
#                 if visited[r][c] + 1 + val < visited[nr][nc]:
#                     visited[nr][nc] = visited[r][c] + 1 + val
#                     que.append((nr, nc))
#     return visited[N-1][N-1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     visited = [[float('inf')] * N for _ in range(N)]
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     bfs(0, 0)
#
#     print(f'#{tc} {visited[N-1][N-1]}')

# # 알뜰 기차 여행
# # distance 최단거리 테이블
import heapq
#
# V, E = map(int, input().split())
# graph = [[] for i in range(V)]
# distance = [float('inf')] * V  # 최단거리 테이블을 모두 초기화(리스트받아서 개수처리)
# visited = [False] * V
# pq = []  # 우선순위 큐
#
# for _ in range(E):
#     from_node, to, cost = map(int, input().split())
#     graph[from_node].append((to, cost))
#
#
# def dijkstra(node):
#     distance[0] = 0  # 시작노드 초기화
#     heapq.heappush(pq, (0, 0))  # (비용, 노드)
#
#     while pq:
#         cur_cost, cur_node = heapq.heappop(pq)  # 우선순위 큐에서 현재노드/비용 가져옴
#         if visited[cur_node]:  # 이미 방문한 노드라면
#             continue
#         visited[cur_node] = True  # 방문처리
#         # 현재 노드와 연결된 다른 노드를 확인
#         for next_node, edge_cost in graph[cur_node]:
#             total_cost = cur_cost + edge_cost  # 총비용 계산
#             if distance[next_node] > total_cost:  # 최단거리 테이블 갱신 조건 확인
#                 distance[next_node] = total_cost
#                 heapq.heappush(pq, (distance[next_node], next_node))  # 우선순위 큐에 새로운 노드 정보 추가
#
# dijkstra()
# if distance[V-1] == float('inf'):
#     print('impossible')
# else:  # 도착지점에 도달하는 비용 출력
#     print(distance[V-1])

# 최소 이동 거리
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

'''
1
2 3
0 1 1
0 2 6
1 2 1

'''