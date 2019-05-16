from tree_node import TreeNode

class PostorderTraversal:
    def traverseRecursive(self, node: TreeNode, vals: List[int]) -> None:
        if node != None:
            if node.left != None:
                self.traverseRecursive(node.left, vals)
            if node.right != None:
                self.traverseRecursive(node.right, vals)
            vals.append(node.val)
    
    def traverse(self, root: TreeNode) -> List[int]:
        vals = []
        self.traverseRecursive(root, vals)
        return vals
