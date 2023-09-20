# # .1 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# def backtracking(num):
#     if num == M:
#         print(*path)
#         return
#     for i in num_list:
#         if i in path:
#             continue
#         path[num] = i
#         backtracking(num+1)
#         path[num] = 0
#
# N, M = map(int, input().split())
# num_list = [i for i in range(N+1)]
# path = [0] * M
# backtracking(0)

# # .2 고른 수열은 오름차순이어야 한다.
# def backtracking(num):
#     if num == M:
#         print(*path)
#         return
#     for i in num_list:
#         if path[num-1] > i:
#             continue
#         if i in path:
#             continue
#         path[num] = i
#         backtracking(num+1)
#         path[num] = 0
#
# N, M = map(int, input().split())
# num_list = [i for i in range(N+1)]
# path = [0] * M
# backtracking(0)

# # 위와 같은거  (남의 코드)
# def func(start):
#     if len(path) == m:
#         print(*path)
#         return
#     for i in range(start, n + 1):
#         if i not in path:
#             path.append(i)
#             func(i + 1)
#             path.pop()
# n, m = list(map(int, input().split()))
# path = []
# dfs(1)

# # .3 같은 수를 여러 번 골라도 된다.
# def backtracking(num):
#     if num == M:
#         print(*path)
#         return
#     for i in range(1, N+1):
#         path[num] = i
#         backtracking(num+1)
#         path[num] = 0
#
# N, M = map(int, input().split())
# path = [0] * M
# backtracking(0)