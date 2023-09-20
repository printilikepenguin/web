#1232

def cal(num):
    if len(nodes[num]) == 4:
        sign, left, right = nodes[num][1], int(nodes[num][2]), int(nodes[num][3])
        if sign == '+':
            return cal(left) + cal(right)
        if sign == '-':
            return cal(left) - cal(right)
        if sign == '*':
            return cal(left) * cal(right)
        if sign == '/':
            return cal(left) / cal(right)
    else:
        return cal(nodes[num][1])


for tc in range(1, 11):
    N = int(input())
    nodes = [input().split() for _ in range(N)]
    print(f'#{tc} {cal(1)}')


'''
def cal(num):
    if len(node[num]) == 4:
        a, b, c = node[num][1], int(node[num][2]), int(node[num][3])
        if a == '+':
            return cal(b) + cal(c)
        elif a == '-':
            return cal(b) - cal(c)
        elif a == '*':
            return cal(b) * cal(c)
        else:
            return cal(b) / cal(c)
    else:
        return int(node[num][1])
 
for t in range(1, 11):
    N = int(input())
    node = [[]] + [input().split() for _ in range(N)]
    print(f'#{t} {int(cal(1))}')
'''
'''
def calc(v):
    if len(T[v]) == 2: 
        return int(T[v][1])
 
    l = calc(int(T[v][2]))
    r = calc(int(T[v][3]))
    
    if T[v][1] == '+': 
        return l + r
    elif T[v][1] == '-': 
        return l - r
    elif T[v][1] == '*': 
        return l * r
    else: 
        return l // r
 
for tc in range(1, 11):
    N = int(input())
    T = [[]]
    for i in range(N):
        T.append(list(input().split()))
 
    print('#{} {}'.format(tc, calc(1)))
'''
#1240

#1242