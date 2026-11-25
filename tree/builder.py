from tree.node import Node


def build_tree():
    """Builds the binary tree (P A U L A N T E Q U I N A) as drawn:

                 P
               /   \\
             A       U
            / \\     / \\
           L   A   N   T
          / \\ / \\
         E  Q U  I
        / \\
       N   A
    """
    root = Node("P")
    root.left = Node("A")
    root.right = Node("U")

    root.left.left = Node("L")
    root.left.right = Node("A")
    root.right.left = Node("N")
    root.right.right = Node("T")

    root.left.left.left = Node("E")
    root.left.left.right = Node("Q")
    root.left.right.left = Node("U")
    root.left.right.right = Node("I")

    root.left.left.left.left = Node("N")
    root.left.left.left.right = Node("A")
    return root
