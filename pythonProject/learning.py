'''
알고리즘 풀이법
1. 완탐 DFS, BFS
2. 상황마다 좋은 거 찾기 Greedy
3. 하나의 큰 문제를 작은 문제로 나누기 DP - Memoization, 점화식, 재귀
4. 큰 문제를 작은 문제로 쪼개기 분할정복
- 퀵정렬
- 이진검색 : 원하는 값 빨리 찾기
5. 전체 중 가능성 없는 걸 빼고보자 빽트래킹 가지치기
'''
'''
# SWEA 병합정렬(분할함수+병합함수)
# 분할함수(재귀)
def divide(arr):
    if len(arr) <= 1:  # 리스트의 길이가 1 이하면 그대로 반환
        return arr
    middle = len(arr) // 2
    left = divide(arr[:middle])
    right = divide(arr[middle:])
    return merge(left, right)
# 병합함수
def merge(left, right):
    global ans
    # 만약 right의 마지막 원소가 left의 마지막 원소보다 작을 경우
    if right[-1] < left[-1]:
    # answer는 1씩 증가
        ans += 1
    result = []  # 병합 결과
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        # 왼쪽과 오른쪽 리스트 모두 남아있는 경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # 왼쪽 리스트만 남아있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1
        # 오른쪽 리스트만 남아있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    result = divide(arr)

    print(f'#{tc} {result[N//2]} {ans}')
'''
'''
# SWEA 퀵정렬(재귀)
def quick(arr, start, end):
    if start >= end:  # 재귀 종료 조건
        return
    pivot = start  # 피벗 위치를 시작 지점으로 설정
    left = start + 1  # 왼쪽 포인터 설정
    right = end  # 오른쪽 포인터 설정

    while left <= right:
        #피벗보다 큰 값을 찾을 때까지 왼쪽 포인터를 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        #피벗보다 작은 값을 찾을 때까지 오른쪽 포인터를 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        #왼쪽 포인터가 오른쪽 포인터보다 크면 피벗과 오른쪽 값을 교환
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 그렇지 않으면 왼쪽값과 오른쪽 값을 교환
            arr[left], arr[right] = arr[right], arr[left]
    # 피벗의 왼쪽 부분 재귀적 정렬
    quick(arr, start, right-1)
    # 피벗의 오른쪽 부분 재귀적 정렬
    quick(arr, right+1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')
'''
'''
# SWEA 이진탐색
def binarySearch(target):
    start, end = 0, n-1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            # 직전에 왼쪽 방향을 검사했다면 탐색 중단
            if check == 1:
                break
            check = 1
            end = mid - 1  # 끝 위치 이동
        else:
            # 직전에 오른쪽 방향을 검사했다면 탐색 중단
            if check == 2:
                break
            check = 2
            start = mid + 1
    return False

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binarySearch(num)
    print(f'#{tc} {total}')
'''
'''
# solivng club 18822
def bianrySearch(target):
    start, end = 0, N
    while start <= end:
        mid = (start+end) // 2
        # 1. 왼쪽 부분 탐색, 중간점의 값이 찾고자하는 값보다 큰 경우
        if A[mid] > target:
            end = mid - 1
        # 2. 오른쪽 부분 탐색, 중간점의 값이 찾고자하는 값보다 작은 경우
        elif A[mid] < target:
            start = mid + 1
        # 3. 중간값이 찾고자하는 값과 같은 경우는 탐색 종료
        elif A[mid] == target:
            return True
    return False

N = int(input())
A = tuple(sorted(list(map(int, input().split()))))
k = int(input())
B = tuple(map(int, input().split()))
for b in B:
    if bianrySearch(b):
        print('O', end='')
    else:
        print('X', end='')
'''
