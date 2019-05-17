from tree_node import TreeNode

class Tree:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftDepth = 0
        rightDepth = 0
        if root.left != None:
            leftDepth = self.maxDepth(root.left)
        if root.right != None:
            rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1
