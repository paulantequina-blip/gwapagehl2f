def print_tree(node, prefix="", label="Root"):
    """Prints the tree sideways, one node per line."""
    if node:
        print(f"{prefix}{label}: {node.data}")
        if node.left or node.right:
            print_tree(node.left, prefix + "    ", "L")
            print_tree(node.right, prefix + "    ", "R")


def fmt(items):
    return " - ".join(items)
