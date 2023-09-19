# # { 1, 2, 3 } 집합에서 3개의 숫자를 선택하는 기본적인 예제
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 1. 기저 조건이 중요 (재귀 종료 조건)
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         return
#     for i in arr:
#     # 2. 들어가기 전 로직 - 경로 저장
#         path[cnt] = i
#     # 3. 다음 재귀 함수 호출
#         backtracking(cnt + 1)
#     # 4. 돌아와서 할 로직
# ################################
# # { 1, 2, 3 } 집합에서 3개의 숫자를 선택하는 기본적인 예제
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 1. 기저 조건이 중요 (재귀 종료 조건)
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         print(*path)
#         return
#     for i in arr:
#     # 2. 들어가기 전 로직 - 경로 저장
#         path[cnt] = i
#     # 3. 다음 재귀 함수 호출
#         backtracking(cnt + 1)
#         print(path)
#     # 4. 돌아와서 할 로직
#         path[cnt] = 0
#
# backtracking(0)
# ####################################
# # { 1, 2, 3 } 집합에서 3개의 숫자를 선택하는 기본적인 예제
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 1. 기저 조건이 중요 (재귀 종료 조건)
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         print(*path)
#         return
#     for i in arr:
#         # 가지치기
#         if i in path:
#             continue  # 중복숫자 제거
#     # 2. 들어가기 전 로직 - 경로 저장
#         path[cnt] = i
#     # 3. 다음 재귀 함수 호출
#         backtracking(cnt + 1)
#     # 4. 돌아와서 할 로직 (여기가 중요행용)
#         path[cnt] = 0  # 초기화
# backtracking(0)
####################################
# def func():
    # 재귀를 끝내는 기저 조건

    # pdf 연습문제 힌트 : 기저조건
    # if acc_sum > 10:
        # return


    # 가지치기 - 조건 작성이 핵심

    # 반복문
        # 가지치기

        # 재귀 들어가기 전
        # 재귀 함수 호출
        # 돌아와서 초기화