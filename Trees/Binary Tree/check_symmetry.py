from tree_node import TreeNode

class BinaryTree:
    # takes two nodes (one for each side of the tree) & recursively calls opposite sides on each
    # the tree is symmetric if each left from node1 equals a right from node2 and vice versa
    def isSymmetricRecursive(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 != None and node2 != None and node1.val == node2.val:
            path1Symmetric = self.isSymmetricRecursive(node1.left, node2.right)
            path2Symmetric = self.isSymmetricRecursive(node1.right, node2.left)
            return (path1Symmetric and path2Symmetric)
        elif node1 == None and node2 == None:
            return True
        else:
            return False
    # checks if a binary tree is symmetric
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSymmetricRecursive(root.left, root.right)
