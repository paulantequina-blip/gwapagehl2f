"""
Assessment 3.6: DFS Methods in Tree
Run this file in PyCharm (right-click -> Run 'main').
"""
from tree.builder import build_tree
from tree import dfs
from tree.display import print_tree, fmt


def show_all(root):
    print("\n=== Recursive DFS ===")
    print("PreOrder  :", fmt(dfs.preorder(root)))
    print("InOrder   :", fmt(dfs.inorder(root)))
    print("PostOrder :", fmt(dfs.postorder(root)))
    print("\n=== Iterative DFS (Stack) ===")
    print("PreOrder  :", fmt(dfs.preorder_iterative(root)))
    print("InOrder   :", fmt(dfs.inorder_iterative(root)))
    print("PostOrder :", fmt(dfs.postorder_iterative(root)))


def menu():
    root = build_tree()
    while True:
        print("\n" + "=" * 40)
        print(" DFS METHODS IN TREE (P A U L A N T E Q U I N A)")
        print("=" * 40)
        print("[1] Display Tree")
        print("[2] PreOrder  (Root-Left-Right)")
        print("[3] InOrder   (Left-Root-Right)")
        print("[4] PostOrder (Left-Right-Root)")
        print("[5] Show All Traversals")
        print("[0] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            print()
            print_tree(root)
        elif choice == "2":
            print("PreOrder  :", fmt(dfs.preorder(root)))
        elif choice == "3":
            print("InOrder   :", fmt(dfs.inorder(root)))
        elif choice == "4":
            print("PostOrder :", fmt(dfs.postorder(root)))
        elif choice == "5":
            show_all(root)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
