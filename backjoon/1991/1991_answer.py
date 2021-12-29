import sys
sys.stdin = open('1991_mode.txt')

N = int(input())

class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

tree = dict()

for i in range(N):
    node, left, right = input().split()
    tree[node] = Node(node, left, right)

def preorder(node):
    print(node.node, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
# def inorder(node):
#     if node.left !='.':
#         inorder(tree[node.left])
#     print(node.node, end = "")
#     if node.right != '.':
#         inorder(tree[node.right])
# def postorder(node):
#     if node.left !='.':
#         postorder(tree[node.left])
#     if node.right != '.':
#         postorder(tree[node.right])
#     print(node.node, end = "")

preorder(tree['A'])
print()
# inorder(tree['A'])
# print()
# postorder(tree['A'])

