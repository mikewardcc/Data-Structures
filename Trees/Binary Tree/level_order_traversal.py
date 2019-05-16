from tree_node import TreeNode

class LevelOrderTraversal:
    # returns a list of lists, where each inner list represents a level in the tree
    def traverse(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level = [root]
        nextLevel = []
        result = []
        while level: # while it's not empty
            vals = []
            for node in level:
                if node == None:
                    continue
                vals.append(node.val)
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            result.append(vals)
            level = nextLevel
            nextLevel = []
        return result
