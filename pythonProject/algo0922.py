# '''
# 1. 문제 해석 : 문제에서 원하는 목표
# 2. 어떤 알고리즘을 쓸까?
#   - 모든 경우의 수를 봐야 한다 : 완탐으로 접근
# '''
#
#
# # 1486
# def backtraking(cnt):
#     if cnt == N:
#         if sum(path) < B:
#             return
#         else:
#             tops.append(sum(path))
#             return
#     for i in H_list:
#         if path[cnt] == i:
#             continue
#         path[cnt] = i
#         backtraking(cnt+1)
#         path[cnt] = 0
# ## 강사님의....
# def recur(level, acc_height):  # 높이와 탑 높이의 합
#     global min_v
#     # 가지치기
#     # 현재 탑이 선반 높이를 넘어간다면
#     # 앞으로 볼 필요가 없당
#     if acc_height >= B:
#         min_v = min(min_v, acc_height)
#         return
#     # 기저조건
#     if level == N:
#         return
#     recur(level+1, acc_height+H_list[level])
#     # 안쓸경우
#     recur(level+1, acc_height)
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     H_list = list(map(int, input().split()))
#     min_v = int(1e9)
#     recur(0, 0)
#
#     print(f'#{tc} {min_v - B}')
# ## 코드ㅡ...
#     path = [0] * N
#     tops = []
#
# # 1952
#
# def dfs(month, acc_cost):
#     global ans
#     # 기저조건
#     if month > 12:
#         ans = min(ans, acc_cost)
#         return
#     if acc_cost > ans:
#         return
#     # 1일 이용권으로 모두 구입
#     # 1달 이용권
#     # 3달 이용권
#     # 1년 이용권
#
# T = int(input())
# for tc in range(1, T+1):
#     day, month, months, year = map(int, input().split())
#     planlist = list(map(int, input().split()))
#     ans = int(1e9)
#
# # 2819
# ## 숫자가 0으로 시작하면 문자열로 처리
# '''
# 재귀 돌리면서 숫자를 붙인다
# 숫자가 7자리가 되면
# 세트에다 넣는다 (중복 제거)
# '''
# dir = [(0,-1),(-1,0),(0,1),(1,0)]
# def bruteforce(y, x, number):
#     if len(number) == 7:
#         result.add(number)
#         return
#     for dy, dx in dir:
#         ny, nx = y+dy, x+dx
#         # 갈 수 없으면 continue
#         if ny<0 or ny>=4:
#             continue
#         if nx<0 or nx>=4:
#             continue
#         # 갈 수 있다면 다음 위치로 ㄱ
#         dfs(ny, nx, number+map[ny][nx])
#
# T = int(input())
# for tc in range(1, T+1):
#     # 서로 다른 수로 합친다 >>> 문자열 레츠고
#     map = [input().split() for _ in range(4)]
#     result = set()
#     # 시작지점 : 전부
#     for i in range(4):
#         for j in range(4):
#             bruteforce(i, j, map[i][j])
#
#     print(f'#{tc} {len(result)}')
#
# # 1238
# # 그림 설명이 bfs, 재연락X는 visited를 의미
# from collections import deque
# def bfs(s):
#     q = s()
#     visited[s] = 1
#     while q:
#         now = q.pop(0)
#         # 갈 수 있는 지점 다 가깅
#         for t in graph[now]:
#
#                 continue
#                 if max_depth
#
#
# for tc in range(1, 11):
#     length, start = map(int, input().split())
#     temp_graph = list(int(input().split()))
#     graph = [[] for _ in range(101)]
#     visited = []
#
#     for i in range(0, n, 2):
# #############################################
# solving club 최소이동거리
import heapq

def dijkstra(start):
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (start, 0))

    while pq:
        dist, now = heapq.heappop(pq)
        for next_node, next_dist in graph[now]:
            total_dist = dist + next_dist
            if distance[next_node] > total_dist:
                distance[next_node] = total_dist
                heapq.heappush(pq, (total_dist, next_node))

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    distance = [int(1e9)] * (N+1)

    dijkstra(0)

    print(f'#{tc} {distance[N]}')

# 강사님 코드

def dijkstra(start):
    dist[start] = 0
    for _ in range(N+1):
        min_idx = -1  # 최소거리 노드의 인덱스
        min_value = float('inf')

        for i in range(N+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1  # 최소거리 노드 방문 처리

        for i in range(N+1):
            if arr[min_idx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[min_idx]+arr[min_idx][i])

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dist = [int(1e9)] * (N+1)
    visited = [False] * (N+1)
    for s,e,w in edges:
        arr[s][e] = w

    dijkstra(0)

    print(f'#{tc} {dist[N]}')

######################
# solving club changyong village
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa > pb:
        pa, pb = pb, pa

    parents[pb] = pa


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 딕셔너리 컴프리헨션: 각 사람에 대해 초기에는 자기 자신을 부모로 설정
    parents = {i: i for i in range(1, N + 1)}
    for i in range(M):
        a, b = map(int, input().split())
        # 두 사람이 다른 그룹에 속해있다면 union 실행
        if find(a) != find(b):
            union(a, b)
    group = set()
    for i in range(1, N + 1):
        # 해당 사람이 그룹에 속해있지 않다면 해당 사람의 최종 그룹을 찾아 set에 추가
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f'#{tc} {len(group)}')

# 다익스트라 탑 N과 M
import heapq
dir = [(0,-1),(-1,0),(1,0),(0,1)]
def dijkstra():
    pq = []
    dist[0][0] = map[0][0]
    heapq.heappush(pq, (map[0][0], 0, 0))

    while pq:
        cost, y, x = heapq.heappop(pq)
        if dist[y][x] < cost:
            continue
        for dy, dx in dir:
            ny, nx = dy+y, dx+x
            # 범위를 벗어날 경우 제외
            if ny<0 or nx<0 or ny>=N or nx>=M:
                continue
            next_cost = cost + map[ny][nx]
            # 이미 발견한 경로가 더 작은 경우 제외
            if dist[ny][nx] <= next_cost:
                continue
            dist[ny][nx] = next_cost
            heapq.heappush(pq, (next_cost, ny, nx))
    return dist[N-1][M-1]

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
dist = [[int(1e9)] * M for _ in range(N)]

print(dijkstra())