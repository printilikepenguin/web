# 정중앙 대학교
# 맥스를 꺼낼 땐 -1을 곱해준다던지의 스킬 ...
import heapq

max_heap = []
min_heap = []
mid = 500

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v) #max heap을 구현을 위해 -1을 곱해준다
    else:
        heapq.heappush(min_heap, v)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap) #max heap에서 값을 꺼낼때 -1을 곱해준다
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid) #max heap에 값을 넣을때 -1을 곱해준다
        mid = heapq.heappop(min_heap)
    print(mid)

# 황금의 개수
import heapq
N = int(input())
arr = list(map(int, input().split()))
que = []  # 황금과 짱돌을 저장할 최소 힙
cnt = 0  # 황금 개수
for i in range(N):
    heapq.heappush(que, [arr[i], -1])  # 각 황금의 무게와 -1을 저장
while que:  # 힙에 요소가 있을 때까지 반복
    x, tp = heapq.heappop(que)  # 힙에서 가장 가까운 돌을 꺼낸다
    if tp == 0:  # 꺼낸 돌이 짱돌이면
        break
    cnt += 1  # 황금을 꺼냈으면 cnt += 1

    y, tp = heapq.heappop(que)
    if tp == 0:  # 꺼낸 돌이 짱돌이면
        break
    else:
        heapq.heappush(que, [y*2, 0])  # 황금 2배 무게의 짱돌돌
    cnt += 1
print(cnt)