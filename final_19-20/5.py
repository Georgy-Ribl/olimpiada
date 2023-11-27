class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(node):
    if node != None:
        print(node.val)  # обработка корня
        preorder(node.left)  # обработка левого узла
        preorder(node.right)  # обработка правого узла


def postorder(node):
    if node != None:
        preorder(node.left)  # обработка левого узла
        preorder(node.right)  # обработка правого узла
        print(node.val)  # обработка корня


postorder(root)
