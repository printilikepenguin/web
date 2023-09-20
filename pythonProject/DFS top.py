# # 오웅 크리스마스 ㅜ
# def inorder_dfs(num):
#     if num <= N:
#         inorder_dfs(num * 2)
#         print(num, end=' ')
#         inorder_dfs(num*2 + 1)
#     else: return
#
# def preorder_dfs(num):
#     if num <= N:
#         print(num, end=' ')
#         preorder_dfs(num*2)
#         preorder_dfs(num*2 + 1)
#     else: return
#
# def postorder_dfs(num):
#     if num <= N:
#         postorder_dfs(num*2)
#         postorder_dfs(num*2 + 1)
#         print(num, end=' ')
#     else: return
#
# N = int(input())
# visited = [0] * N
# arr = []
# for _ in range(N):
#     num, left, right = map(int, input().split())
#     if left == -1:
#         arr.append([right])
#     elif right == -1:
#         arr.append([left])
#     elif left == -1 and right == -1:
#         arr.append([])
#     else:
#         arr.append([left, right])
#
# print(inorder_dfs(1))
# print(preorder_dfs(1))
# print(postorder_dfs(1))
# #########################################
# # 개에바 강사님 코드 ㅡㅡ
# tree = [[-1,-1] for _ in range(1001)]
# N = 0
# preorder, inorder, postorder = [], [], []
#
# def dfs(now):
#     # now가 -1이면 return
#     if now == -1:
#         return
#     # 전위
#     preorder.append(now)
#     # 왼쪽
#     dfs(tree[now][0])
#     # 중위(왼->루트->오른)
#     inorder.append(now)
#     # 오른쪽
#     dfs(tree[now][1])
#     # 후위(왼->오->루트)
#     postorder.append(now)
#
# N = int(input())
# for _ in range(N):
#     root, l, r = map(int, input().split())
#     tree[root][0] = l
#     tree[root][1] = r
# print(tree)
# dfs(1)
# print(' '.join(map(str, inorder)))
# print(' '.join(map(str, preorder)))
# print(' '.join(map(str, postorder)))
# ############################################
# # 반장님 코드
# def inorder(start):
#     stack = tree_dict[start][:]
#     if stack[0] != -1:
#         inorder(stack[0])
#     print(start, end=" ")
#     if stack[1] != -1:
#         inorder(stack[1])
#
#
# def preorder(start):
#     stack = tree_dict[start][:]
#     print(start, end=" ")
#     while stack:
#         check = stack.pop(0)
#         if check != -1:
#             preorder(check)
#
#
# def postorder(start):
#     stack = tree_dict[start][:]
#     while stack:
#         check = stack.pop(0)
#         if check != -1:
#             postorder(check)
#     print(start, end=" ")
#
#
# N = int(input())
#
# tree_dict = {}
#
# for _ in range(N):
#     start, left, right = map(int, input().split())
#     tree_dict[start] = [left, right]
#
# inorder(1)
# print()
# preorder(1)
# print()
# postorder(1)
# ###################################################
# ############################################
# # Finding the ranking
#
# # 학생수, 질문 횟수, 출력해야하는 학생 번호
# N, M, X = map(int, input().split())
#
# up_v = [[] for _ in range(N+1)]  # 어떤 학생이 다른 학생보다 잘했는지
# down_v = [[] for _ in range(N+1)]  # 어떤 학생보다 더 잘한 학생
#
# #up : 타겟보다 못한 학생 수, down: target보다 잘한 학생 수
# up = down = 1  # 자기 자신도 더해야하기 땜에 1로 초기화
#
# up_used = [False] * (N+1)
# down_used = [False] * (N+1)
#
# # 타켓보다 못한 학생들을 탐색하는 dfs 함수
# def up_dfs(node):
#     global up
#     for next_node in up_v[node]:  # 노드보다 못한 학생들 순회
#         if not up_used[next_node]:  # 아직 방문X 라면
#             up += 1
#             up_used[next_node] = True  # 방문표시
#             up_dfs(next_node)
#
# def down_dfs(node):
#     global down
#     for next_node in down_v[node]:
#         if not down_used[next_node]:
#             down += 1
#             down_used[next_node] = True
#             down_dfs(next_node)
#
# for _ in range(M):
#     A, B = map(int, input().split())
#     up_v[B].append(A)
#     down_v[A].append(B)
#
# up_dfs(X)
# down_dfs(X)
#
# print(up)
# print(N-down + 1)  # 낮은 둥수
#
#########################################################################################
# # The two Robots
#
# #동굴의 방 개수, 두로봇이 위치한 방 번호
# N, s, e = map(int, input().split())
# al = [[] for _ in range(N + 1)] #al 리스트는 각 방과 연결된 방의 정보
# visited = [0 for _ in range(N + 1)] # visited리스트 : 해당 방을 방문했는지 여부
# sum_v = 0
# MIN = float('inf')
# MAX = float('-inf')
# #주어진 시작위치(node) 부터 목표위치(dest)까지 이동하는 모든 경로 탐색
# def dfs(node, dest):
#     global sum_v, MIN, MAX
#     #만약 목표위치에 도달하면, 최솟값(이동한 거리 - 가장 긴 통로의 길이) 확인
#     if node == dest:
#         if sum_v - MAX < MIN:
#             MIN = sum_v - MAX
#         return
#     for next in al[node]:
#         if visited[next[0]] == 1: #이미 방문한 방은 다시 방문 x
#             continue
#         sum_v += next[1]
#         visited[next[0]] = 1
#         temp = MAX
#         #지금까지 방문한 통로중 가장 긴것을 MAX에 저장
#         if next[1] > MAX:
#             MAX = next[1]
#         dfs(next[0], dest)
#         #dfs호출 후 이전 상태로 복원
#         visited[next[0]] = 0
#         sum_v -= next[1]
#         MAX = temp
# for _ in range(N - 1):
#     from_v, to_v, cost = map(int, input().split())
#     al[from_v].append((to_v, cost))
#     al[to_v].append((from_v, cost))
# visited[s] = 1 #dfs탐색 전에 로봇이 위치한 방 방문 처리
# dfs(s, e)
# #만약 두 로봇이 이미 통신이 가능한 위치에 있으면 0을 출력
# print(MIN if MIN != float('inf') else 0)
################################################################
# Dongchul

# 현재직원 n, 일 할당받은 직원 리스트 items, 성공확률 total
def DFS(n, items, total):
    global ans
    # 현재 확률이 이미 알려진 최대확률보다 낮으면 탐색x
    if total <= ans:
        return
    # 모든 직원에게 일이 할당되면 최대확률 갱신
    if n == N:
        ans = max(ans, total)
        return
    for i in range(N):
        if i not in items:  # 해당 직원이 아직 일을 할당받지 않았다면
            items.append(i)  # 일 할당하고
            DFS(n+1, items, total*(arr[n][i]/100))
            items.pop()  # 백트래킹 : 할당 해제

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    DFS(0, [], 1)  # 첫번째 직원부터 시작하여 dfs 호출
    result = round(ans*100, 6)
    print(f'#{tc} {result}')