# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        m = 0
        def helper(root):
            nonlocal m
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)
            m = max(m,lh+rh)

            return 1 + max(lh,rh)
        helper(root)
        return m