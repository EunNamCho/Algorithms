import sys

input = sys.stdin.readline

def preorder(node):
    if node == '.':
        return
    print(node, end='')      # 루트
    preorder(tree[node][0])  # 왼쪽
    preorder(tree[node][1])  # 오른쪽

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])   # 왼쪽
    print(node, end='')      # 루트
    inorder(tree[node][1])   # 오른쪽

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) # 왼쪽
    postorder(tree[node][1]) # 오른쪽
    print(node, end='')      # 루트

# 입력 처리
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# 결과 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')