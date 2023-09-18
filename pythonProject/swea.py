# def binarySearch(arr, target):
#     start, end = 0, N
#     while start <= end:
#         mid = (start+end) // 2
#         if arr[mid] > target:
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#         elif arr[mid] == target:
#             return True
#     return False

def binary_search(target, data):
    start, end = 0, len(data)-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N, Q = map(int, input().split())  # 광물 개수, 연구원 수
n_list = sorted(list(map(int, input().split())))  # N개의 광물에 대한 상대 강도
for _ in range(Q):
    s, e = map(int, input().split())
    cnt = 0
    for i in range(s, e):
        cnt += binary_search(i, n_list)
    print(cnt)

'''
10 5
1 2 2 2 2 3 4 3 4 -1
2 3
-1000000000 1000000000
-10 0
2 4
2 2
'''