class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #basically bigger numbers on left and smaller on right
        if not root:
            return None

        #swapping children 
        root.left, root.right = root.right, root.left

        #making recursive calls for children further down
        self.invertTree(root.left)     #invert left sidwe
        self.invertTree(root.right)    #invert right side both a recusrive cals 
        return root 