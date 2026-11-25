"""DFS methods in a binary tree: PreOrder, InOrder, PostOrder."""


# ---------- Recursive ----------
def preorder(node, result=None):
    """Root -> Left -> Right"""
    if result is None:
        result = []
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    """Left -> Root -> Right"""
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    """Left -> Right -> Root"""
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result


# ---------- Iterative (stack) ----------
def preorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_iterative(root):
    result, stack, current = [], [], root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    return result


def postorder_iterative(root):
    result, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]
