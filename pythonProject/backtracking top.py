# # sum of one, two, three
#
# N = int(input())
# cnt = 0
#
# def func(num):
#     global cnt
#     if num == N:  # N에 도달했다면 하나의 경우의 수를 더 찾았다
#         cnt += 1
#         return
#     if num > N:  # num이 N을 넘어가면 no...
#         return
#     # 재귀구성: 1,2,3 더해서 다음 구성으로 넘어가깅
#     for i in range(1, 4):
#         func(num+i)
#
# func(0)
# print(cnt)
#
# DP로 풀었을 때
#    DP = [1, 2, 4]
#     N = int(input())
#     for i in range(3,N):
#         DP.append(DP[i-1]+DP[i-2]+DP[i-3])
#     print(DP[N-1])
#
# #######################
#
# # throwing a dice
# N, M = map(int, input().split())
# path = [0] * 10  # 주사위를 던져 나온 값을 저장하는 path 리스트
#
# def printpath(level):
#     print(' '.join(map(str, path[:level])))  # 주사위값 문자열 변경 후 공백 넣어 출력
#
# def roll1(level):  # M=1일 때
#     if level == N:  # 주사위를 N번 던졌다면 결과출력
#         printpath(level)
#         return
#     for i in range(1, 7):
#         path[level] = i  # 현 레벨의 주사위값을 i로 설정
#         roll1(level + 1)  # 다음 레벨로 재귀 호출
#         path[level] = 0  # 백트래킹 : 현재 레벨의 주사위값 초기화
#
# def roll2(level):  # M=2일 때
#     if level == N:  # 주사위를 N번 던졌다면 결과출력
#         printpath(level)
#         return
#     for i in range(1, 7):
#         # 중복 제거 조건
#         if level > 0 and i < path[level - 1]:
#             continue
#         path[level] = i  # 현 레벨의 주사위값을 i로 설정
#         roll2(level + 1)  # 다음 레벨로 재귀 호출
#         path[level] = 0  # 백트래킹 : 현재 레벨의 주사위값 초기화
#
# DAT = [0] * 10
#
# def roll3(level):  # M=3 일 때
#     if level == N:  # 주사위를 N번 던졌다면 결과출력
#         printpath(level)
#         return
#     for i in range(1, 7):
#         # 사용한 눈금 스킵할건뎅
#         if DAT[i] == 1:
#             continue
#         DAT[i] = 1  # 현재 레벨에서 눈금 사용 쳌
#         path[level] = i  # 현 레벨의 주사위값을 i로 설정
#         roll2(level + 1)  # 다음 레벨로 재귀 호출
#         path[level] = 0  # 백트래킹 : 현재 레벨의 주사위값 초기화
#         DAT[i] = 0  # 백트래킹 : i 눈금 사용 초기화
#
# if M == 1:
#     roll1(0)
# elif M == 2:
#     roll2(0)
# elif M == 3:
#     roll3(0)
#
# ######################################################
#
# # N castle
#
# N = int(input())
# DAT = [0] * 10
# cnt = 0
# def func(row):
#     global cnt
#     # N-1번 행까지 모두 castle 을 각 행에 두었다면
#     if row == N:
#         cnt += 1  # 하나의 조합을 찾았으니 cnt += 1
#         return
#     for col in range(N):
#         # 가지치기: 이미 이 col에 캐슬을 둔 적이 있다면
#         if DAT[col] == 1:
#             continue
#         DAT[col] = 1  # 현재 행에서 경로 저장
#         func(row + 1)  # 재귀 호출
#         DAT[col] = 0  # 초기화
# func(0)
# print(cnt)
#
##################################################
#
# 전기버스 2
#
# def electric(idx, s):
#     global answer
#     if answer < s:
#         return
#     if idx >= N:
#         answer = s
#         return
#     count = N_stops[idx]
#     for i in range(count, 0, -1):
#         electric(idx+i, s+1)
#
# T = int(input())
# for tc in range(1, T+1):
#     answer = 21e8
#     # 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi (ex 5 2 3 1 1)
#     N_stops = list(map(int, input().split()))
#     # 첫번째 값은 정류장의 수, 따로 저장
#     N = N_stops.pop(0) - 1
#     # 0부터 시작하니까 -1
#     electric(0, -1)
#     print(f'#{tc} {answer}')
#
# #####################################

# 최소 생산 비용

def func(cur, total):
    global min_v
    # 가지치기 쭈고
    if total > min_v:
        return
    # 최소비용 업데이트
    if cur == N:
        min_v = min(min_v, total)
        return
    # 현재 제품을 각 공장에 할당하는 경우 모두 고려
    for i in range(N):
        if visited[i] == 1:  # 해당 공장이 이미 할당된 경우 생략
            continue
        visited[i] = 1
        func(cur+1, total+arr[cur][i])
        visited[i] = 0  # 백트래킹 : 할당 취소

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    min_v = float('inf')
    func(0,0)  # 첫번째 제품부터 시작
    print(f'#{tc} {min_v}')