# def binary_search(target, data):
#     global cnt
#     start, end = 0, len(data)
#     while start <= end:
#         mid = (start + end) // 2
#         if data[mid] == target:
#             cnt += 1
#             return  # 함수를 끝내버린다.
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return
#
# N, Q = map(int, input().split())  # 광물 개수, 연구원 수
# n_list = sorted(list(map(int, input().split())))  # N개의 광물에 대한 상대 강도
# cnt = 0
# s, e = -10, 0
# for _ in range(Q):
#     s, e = map(int, input().split())
#     for i in range(s, e+1):
#         a = binary_search(i, n_list)
#
# print(a)
#
# '''
# 10 5
# 1 2 2 2 2 3 4 3 4 -1
# 2 3
# -1000000000 1000000000
# -10 0
# 2 4
# 2 2
# '''
# #################################################

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())