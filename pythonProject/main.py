T = int(input())
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
'''
1
3
73 21 21
11 59 40
24 31 83
'''
print(min(arr))