'''
Tree
- 사이클이 없는 연결 그래프
- 사이클
- 연결그래프 : 모든 꼭지점이 서로 갈 수 있다.
이진 Tree
- 자녀 노드가 둘 이하인 트리
- 종류
  완전 이진 트리 :  # 우리가 신경을 좀 써야할 것
  마지막 레벨을 제외한 모든 레벨은 꽉 차있어야 한다
  마지막 레벨 노드는 왼쪽부터 채워져야 한다
  포화 이진 트리 :
  모든 레벨이 꽉 차있는 것
  나머지 이진 트리 :
  위에 두 개 빼고 다
- 순회방법과 트리 저장 방법이 핵심
  순회방법 :
    전위 : 부모 >>> 좌 >>> 우
    중위 : 좌 >>> 부모 >>> 우
    후위 : 좌 >>> 우 >>> 부모
'''

# pdf 연습문제3
arr = [1,2, 1,3, 2,4, 3,5, 3,6]

# 일차원 배열에 저장하깅 - 잘안씀
# N * 2 + 1 왼쪽 / N * 2 + 2 오른쪽

# 인접리스트로 저장하기
nodes = [[] for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

for i in range(len(nodes)):
    print(nodes[i])

# 자식이 더 이상 없다는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(none)

def preorder(nodeNmbrer):


# 연결리스트로 저장하깅
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입함수
    def insert(self, childNode):
        #  왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        #  오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        return

    # 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            print(self.value, end='')
            # 왼쪽 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 중위 순회 위치 print(self.value, end='')
            # 오른쪽 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()
## 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])
# 연결리스트로 저장하깅
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입함수
    def insert(self, childNode):
        #  왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        #  오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        return

    # 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            print(self.value, end='')
            # 왼쪽 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 중위 순회 위치 print(self.value, end='')
            # 오른쪽 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()
## 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])
#############
# 삭제 트리 .. 후보군을 찾아와야햄
# 각 서브트리에서 가능한 데이터를 찾아와야 한다
# . 왼쪽 서브트리의 가장 오른쪽 자식 노드 ..
# 오른쪽 서브트리의 가장 왼쪽 자식