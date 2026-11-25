import unittest
from tree.builder import build_tree
from tree import dfs


class TestDFS(unittest.TestCase):
    def setUp(self):
        self.root = build_tree()

    def test_preorder(self):
        self.assertEqual("".join(dfs.preorder(self.root)), "PALENAQAUIUNT")

    def test_inorder(self):
        self.assertEqual("".join(dfs.inorder(self.root)), "NEALQAUAIPNUT")

    def test_postorder(self):
        self.assertEqual("".join(dfs.postorder(self.root)), "NAEQLUIAANTUP")

    def test_iterative_matches_recursive(self):
        self.assertEqual(dfs.preorder(self.root), dfs.preorder_iterative(self.root))
        self.assertEqual(dfs.inorder(self.root), dfs.inorder_iterative(self.root))
        self.assertEqual(dfs.postorder(self.root), dfs.postorder_iterative(self.root))


if __name__ == "__main__":
    unittest.main()
