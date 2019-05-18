from tree_node import TreeNode

# see if a path exists that adds up to the goal sum
class BinaryTree:
    def hasPathSum(self, node: TreeNode, goal: int) -> bool:
        if node == None:
            return False
        if goal == node.val and node.left == None and node.right == None:
            return True
        leftPath = False
        rightPath = False
        if node.left != None:
            leftPath = self.hasPathSum(node.left, goal - node.val)
        if node.right != None:
            rightPath = self.hasPathSum(node.right, goal - node.val)
        return (leftPath or rightPath) # if either path is true
