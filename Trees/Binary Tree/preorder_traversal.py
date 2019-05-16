from tree_node import TreeNode

class PreorderTraversal:
	def traverseRecursive(self, node: TreeNode, vals: List[int]) -> None:
		if node != None:
			vals.append(node.val)
			if node.left != None:
				self.traverseRecursive(node.left, vals)
			if node.right != None:
				self.traverseRecursive(node.right, vals)
    
	def traverse(self, root: TreeNode) -> List[int]:
		vals = []
		self.traverseRecursive(root, vals)
		return vals
