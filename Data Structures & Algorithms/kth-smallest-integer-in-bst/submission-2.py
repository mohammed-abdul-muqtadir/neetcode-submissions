# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c, r = k, root.val

        def dfs(root):
            nonlocal c,r
            if not root:
                return

            dfs(root.left)
            if c == 0:
                return
            c -= 1
            if c == 0:
                r = root.val
                return


            dfs(root.right)

        
        dfs(root)
        return r
        

     
