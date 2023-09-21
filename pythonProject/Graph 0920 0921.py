# 인접 행렬과 인접 리스트

# 인접행렬
# arr =  0 1 2 3 4
arr = [
        [0,1,0,1,0],
        [1,0,1,1,1],
        [0,1,0,0,0],
        [1,1,0,0,1],
        [0,1,0,1,0]]
# if arr[0][1] == 1:
# 장점: 구현쉬워  # 단점: 메모리 쉣

# 인접리스트 : 갈 수 있는 지점만 저장하자 ..(인접행렬에서 1만 저장)
# arr =  0 1 2 3 4
arr = [[1,3],
       [0,2,3,4],
       [1],
       [0,1,4],
       [1,3]]
# 단점: 각 노드마다 갈 수 있는 지점 개수가 다르기 땜에 out of range 주의 필요
# 장점: 메모리 효율 미쳤다 <<< 코테를 위해 익숙해지는 게 좋음

# 딕셔너리로도 씁니다 (문자열 받을 때 굿)
# arr = {'0':[1,3],'1':[0,2,3,4],'2':[1],'3':[0,1,4],'4':[1,3]}
#########################################################
# DFS의 1. 스택버전, 2. 재귀버전

# 1. 스택
def dfs_stack(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        # 방문 안했다면 방문 표시
        visited.append(now)
        # 갈 수 있는곳들을 스택에 추가
        for next in range(5):
        # for next in range(4, -1, -1):  # 작은 번호부터 조회 <<< stack.pop(0)은 왜 안될까요?
            # 연결이 안되어 있다면 continue
            if arr[now][next] == 0:
                continue
            # 방문한 지점이면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited

print("dfs stack = ", end='')
print(*dfs_stack(0))

# 2. 재귀
# MAp 크기/길이를 알 때 append말고 아래와 같이 사용하면 훨 빠르다
visited = [0] * 5
path = []  # 방문 순서 기록

def dfs(now):
# 순서 : 1) 기저 조건 2) 들어가기 전 3) 함수 호출 4) 돌아와서 ...
    visited[now] = 1  # 현지점 방문 표시
    print(now, end=' ')
    # 인접한 노드들을 방문
    for next in range(5):
        if arr[now][next] == 0:
            continue
        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end='')
print(dfs(0))
#####################################################
# 인접리스트버전 dfs 스택

# 작은 번호부터 조회
for to in range(len(arr[now])-1, -1, -1):
    # 연결되지 않으면 애초에 리스트에 포함되어 있지 않으므로 체크 필요X
    '''
    # 연결이 안되어 있다면 continue
    if arr[now][next] == 0:
        continue
    '''
    next = arr[now][to]  # 인접리스트는 인덱스랑 next가 같을 수 없음 ,,
    # 방문한 지점이면 stack에 추가하지 않음
    if next in visited:
        continue
###

# 인접리스트 버전 dfs 재귀
# 인접한 노드들을 방문
for to in range(len(arr[now])):
    next = arr[now][to]
'''    if arr[now][next] == 0:
        continue  <<< 필요없다 이제'''
    if visited[next]:
        continue
##############################################
# 완전 이진트리 전중후위 탐색
def inorder_dfs(num):
    if num <= N:
        inorder_dfs(num * 2)
        print(num, end=' ')
        inorder_dfs(num*2 + 1)
    else: return

def preorder_dfs(num):
    if num <= N:
        print(num, end=' ')
        preorder_dfs(num*2)
        preorder_dfs(num*2 + 1)
    else: return

def postorder_dfs(num):
    if num <= N:
        postorder_dfs(num*2)
        postorder_dfs(num*2 + 1)
        print(num, end=' ')
    else: return

##############################################
# BFS ...
# 내가 방문을 했어... 갈 수 있으면 다 방문해주야함

def bfs(start):
    visited = [0] * 5
    # 먼저 방문했던 것을 먼저 처리해줘야 한다 <<< 그래서 큐 쓴다
    queue = [start]
    visited[start] = 1
    # 방문할 지점이 없어질 때까지
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        # 갈 수 있는 곳들은 큐에 추가
        for next in range(5):
            # 연결 X
            if arr[now][next] == 0:
                continue
            # 방문 already
            if visited[next]:
                continue
            # 추가
            queue.append(next)
            # 방문 표시 <<< 이건 위치 위로 옮겨도 ㄱㅊ(bfs라서~!)
            visited[next] = 1
bfs(0)
####################################################

# 서로소 집합들

# 1) 대표자 저장(같은 그룹으로 묶기)
# 2) 각 요소가 내가 속한 그룹의 대표자를 어떻게 찾을지 ..

# make-set 아무것도 없는 것에서 데이터 추가: 원소1개도 집합이다 ..
# union 같은 그룹으로 묶어주깅
# find-set 너 대표가 누구닝 : find-set(y) return x

# 구현방법
# 1) 연결리스트: 데이터 추가될 때 취약함 ..
# 2) 트리: 내 노드가 대표자를 가리킨다

# 예제 레츠고 0 ~ 9

# make-set : 집합 만들어주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]
# find-set  부모를 찾아서 ...
def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])
    # # 경로압축 (0-1-2-3-4-5 >>> 0-1,0-2,0-3,0-4,0-5)
    # parent[x] = find_set(parent[x])
    # return parent[x]
# union 같은 집합으로 묶는 건
def union(x, y):
    # 1. 이미 같은 집합인지 쳌
    x = find_set(x)
    y = find_set(y)  # 너네 대표 찾아와~~
    # 같으면 같은 집합이니까 끝내
    if x == y :
        print("사이클 발생")  # 요 부분 이용해서 발생시 행동 저장 가능
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정
    # parent[y] = x  # 이거하면 끝나긴 하는데
    # 통일성을 위해 아래와 같이 변경합니다
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 예제 실행
union(0,1)
union(2,3)
union(1,3)
# 대표자 검색
print(find_set(2))
print(find_set(3))
# 같은 그룹인지 판별
t_x = 0
t_y = 2
if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다')
else:
    print(f'{t_x}와 {t_y}는 다른 집합에 속해 있습니다')
#############################################################

# 0921
# 신장 트리란?
# 1. 모든 정점을 연결
# 2. 사이클이 존재하지 않는 부분 그래프 - 간선의 개수 : N-1개
# 3. 한 그래프에서 여러개의 신장 트리가 나올 수 있다 ***

# 최소 신장 트리 : 신장트리 중에서 간선들의 가중치 합이 최소인 신장 트리

# Prim 알고리즘: 하나의 정점에서 연결된 간선들 중 하나씩 선택
'''2. Prim MST 알고리즘
시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법

정점 선택을 기반으로 하는 알고리즘이다.
이전 단계에서 만들어진 신장 트리를 확장하는 방법이다.
[과정]

시작 단계에서는 시작 정점만이 MST(최소 비용 신장 트리) 집합에 포함된다.
앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
즉, 가장 낮은 가중치를 먼저 선택한다.
위의 과정을 트리가 (N-1)개의 간선을 가질 때까지 반복한다.
참고 구체적인 내용은 Prim MST 알고리즘이란 참고
https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html'''

'''
7, 11 : 정점과 간선 개수
0 1 32 : 출발점 , 도착점 , 값
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

import heapq
# 힙큐 최대값 꺼낼 때: 음수값으로 넣어주고 꺼낼때 -heapq.heappop() 하면 됨

def prim(start):
    heap = []
    # MST 에 포함되었는지 여부를 관리해주야함
    MST = [0] * V
    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 방문한 노드라면 pass
        if MST[v]:
            continue
        # 방문 체크
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없다면/이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))
    return sum_weight

V, E = map(int, input().split())
# 오늘은 인접행렬
graph = [[0]*V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w  # 하나만 쓰면 단방향
    graph[t][f] = w  # 둘다 쓰면 양방향(무방향)

result = prim(0)
print(f'최소비용 = {result}')

# ####################################################

# KRUSKAL 알고리즘 그리디 중 하나 ...
# 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자

V, E = map(int, input().split())
edge = []  # 간선들 정보
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f,t,w])
# w 를 기준으로 정렬
edge.sort(key=lambda x:x[2])

# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        print('사이클 발생')
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if cnt == V:
            break

#######################################################

# 최단 경로
# 문제유형1: 특정지점 > 도착지점까지의 최단 거리
# 문제유형 가중치에 음수가 포함되어 있다면 > 밸만 포드
# 여러 지점 > 여러 지점가지의 최단 거리 :

# 다익스트라 .. Dijkstra
# 내가 갈 수 있는 경로 주ㅇ 누적거리가 젤 짧은 것부터 고르자
import heapq

# 입력
n, m = map(int, input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 누적거리 계속 저장,
INF = int(1e9)
distance = int(INF) * n

def dijkstra(start):
# 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        # 현 시점에서
        # 누적거리가 젤 잡은 과거 정보 하나 꺼내

    # 이미 방문한 지점 + 누적거리가 더 ㅈ
        if distance[now] < dist:
            continue

        # 인접노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적거리가 기존보다 크면
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)