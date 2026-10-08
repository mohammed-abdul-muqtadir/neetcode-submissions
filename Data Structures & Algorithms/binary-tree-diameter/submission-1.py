# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        
        def helper(node):
            # returns (height, diameter)
            if not node:
                return 0, 0

            lh, ld = helper(node.left)
            rh, rd = helper(node.right)

            curr_height = 1 + max(lh, rh)
            curr_diameter = max(lh + rh, ld, rd)

            return curr_height, curr_diameter

        return helper(root)[1]


