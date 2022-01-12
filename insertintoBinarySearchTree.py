class BSTInserter:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            root = TreeNode(val)
            return root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root