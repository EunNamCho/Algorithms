import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class Node:
    def __init__(self,item):
        self.item = item
        self.left, self.right = None, None
        
class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def put(self,node):
        if self.size==0:
            self.root = node
        else:
            cur = self.root
            while True:
                if cur.item > node.item:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = node
                        break
                if cur.item < node.item:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = node
                        break
        self.size += 1
        
    def traversal(self,node):
        left,right = node.left, node.right
        if left is not None:
            self.traversal(left)
        if right is not None:
            self.traversal(right)
        print(node.item)
            
def main():
    # Input
    bst = BST()
    while True:
        item = input().rstrip()
        if item=="": break
        node = Node(int(item))
        bst.put(node)
    bst.traversal(bst.root)

main()