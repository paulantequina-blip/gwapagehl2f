# Algorithm: DFS Methods in Tree

DFS goes as deep as possible down one branch before backtracking.

PREORDER(node): if node is NULL return; visit(node); PREORDER(left); PREORDER(right)
INORDER(node): if node is NULL return; INORDER(left); visit(node); INORDER(right)
POSTORDER(node): if node is NULL return; POSTORDER(left); POSTORDER(right); visit(node)

Iterative PreOrder: push root; while stack not empty: pop, visit, push right, push left.

Time: O(n)   Space: O(h)
